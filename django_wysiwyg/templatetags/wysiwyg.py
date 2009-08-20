from django.template.defaultfilters import stringfilter
from django.template import Context, Template
from django.template.loader import get_template
from django import template

register = template.Library()

@register.inclusion_tag("django_wysiwyg/includes.html")
def wysiwyg_setup(protocol="http"):
    """
    Create the <style> and <script> tags needed to initialize the rich text editor.

    Create a local django_wysiwyg/includes.html template if you don't want to use Yahoo's CDN
    """
    return {"protocol": protocol}


@register.inclusion_tag('django_wysiwyg/editor.html')
def wysiwyg_editor(field_id, editor_name=None):
    """
    Turn the textarea #field_id into a rich editor. If you do not specify the
    JavaScript name of the editor, it will be derived from the field_id.

    If you don't specify the editor_name then you'll have a JavaScript object
    named "<field_id>_editor" in the global namespace. We give you control of
    this in case you have a complex JS environment.
    """

    if not editor_name:
        editor_name = "%s_editor" % field_id

    return {'field_id':field_id, "editor_name": editor_name}
