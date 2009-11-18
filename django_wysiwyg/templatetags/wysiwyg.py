from urlparse import urljoin

from django import template
from django.conf import settings
from django.template import Context, Template
from django.template.defaultfilters import stringfilter
from django.template.loader import get_template, render_to_string

register = template.Library()

def get_settings():
    """Utility function to retrieve settings.py values with defaults"""
    return {
        "DJANGO_WYSIWYG_MEDIA_URL": getattr(settings, "DJANGO_WYSIWYG_MEDIA_URL", urljoin(settings.MEDIA_URL, "ckeditor/")),
        "DJANGO_WYSIWYG_FLAVOR":    getattr(settings, "DJANGO_WYSIWYG_FLAVOR", "yui"),
        }


@register.simple_tag
def wysiwyg_setup(protocol="http"):
    """
    Create the <style> and <script> tags needed to initialize the rich text editor.

    Create a local django_wysiwyg/includes.html template if you don't want to use Yahoo's CDN
    """

    ctx = {
        "protocol": protocol,
    }
    ctx.update(get_settings())

    return render_to_string(
        "django_wysiwyg/%s/includes.html" % ctx['DJANGO_WYSIWYG_FLAVOR'],
        ctx
    )


@register.simple_tag
def wysiwyg_editor(field_id, editor_name=None):
    """
    Turn the textarea #field_id into a rich editor. If you do not specify the
    JavaScript name of the editor, it will be derived from the field_id.

    If you don't specify the editor_name then you'll have a JavaScript object
    named "<field_id>_editor" in the global namespace. We give you control of
    this in case you have a complex JS ctxironment.
    """

    if not editor_name:
        editor_name = "%s_editor" % field_id

    ctx = {
        'field_id':     field_id,
        'editor_name':  editor_name
    }
    ctx.update(get_settings())

    return render_to_string(
        "django_wysiwyg/%s/editor_instance.html" % ctx['DJANGO_WYSIWYG_FLAVOR'],
        ctx
    )