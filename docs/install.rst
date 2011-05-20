============
Installation
============

in settings.py::

    INSTALLED_APPS = (
        ...
        'django_wysiwyg'
        ...
    )
    
Other settings::

    DJANGO_WYSIWYG_FLAVOR = 'yui'       # Default
    # DJANGO_WYSIWYG_FLAVOR = 'ckeditor'  # Requires you to also place the ckeditor files here:
    # DJANGO_WYSIWYG_MEDIA_URL = "%s/ckeditor" % MEDIA_URL

The following editors are supported out of the box:

* *yui*           - The YAHOO editor.
* *yui_advanced*  - The YAHOO editor with more toolbar buttons.
* *ckeditor*      - The CKEditor, formally known as FCKEditor

It's also possible to add new editors, see :doc:`extending django-wysiwyg <extending>`

