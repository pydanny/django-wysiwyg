from django import template
from django.conf import settings
from django.template.loader import render_to_string

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

register = template.Library()


def get_settings():
    """Utility function to retrieve settings.py values with defaults"""
    flavor = getattr(settings, "DJANGO_WYSIWYG_FLAVOR", "yui")

    return {
        "DJANGO_WYSIWYG_MEDIA_URL": getattr(settings, "DJANGO_WYSIWYG_MEDIA_URL", urljoin(settings.STATIC_URL, flavor) + '/'),
        "DJANGO_WYSIWYG_FLAVOR":    flavor,
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
def wysiwyg_editor(field_id, editor_name=None, config=None):
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
        'editor_name':  editor_name,
        'config': config
    }
    ctx.update(get_settings())

    return render_to_string(
        "django_wysiwyg/%s/editor_instance.html" % ctx['DJANGO_WYSIWYG_FLAVOR'],
        ctx
    )


@register.simple_tag
def wysiwyg_static_url(appname, prefix, default_path):
    """
    Automatically use an prefix if a given application is installed.
    For example, if django-ckeditor is installed, use it's STATIC_URL/ckeditor folder to find the CKEditor distribution.
    When the application does not available, fallback to the default path.

    This is a function for the internal templates of *django-wysiwyg*.
    """
    if appname in settings.INSTALLED_APPS:
        return urljoin(settings.STATIC_URL, prefix)
    else:
        return default_path
