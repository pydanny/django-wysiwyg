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