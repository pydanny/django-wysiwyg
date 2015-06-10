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
    DJANGO_WYSIWYG_FLAVOR = 'ckeditor'  # Requires you to also place the ckeditor files here:
    DJANGO_WYSIWYG_MEDIA_URL = STATIC_URL + "ckeditor/"

The following editors are supported out of the box:

* *ckeditor*         - The CKEditor_, formally known as FCKEditor.
* *redactor*         - The Redactor_ editor (requires a license).
* *tinymce*          - The TinyMCE_ editor, in simple mode.
* *tinymce_advanced* - The TinyMCE_ editor with many more toolbar buttons.
* *yui*              - The YAHOO_ editor (the default)>
* *yui_advanced*     - The YAHOO_ editor with more toolbar buttons.

Media sources
~~~~~~~~~~~~~

When you use one of the editors, you need to make sure that the editor distributables
are also located in your project. By default *django-wysiwyg* looks for a `STATIC_URL/flavor` folder.
You can also install django-ckeditor_ or django-tinymce_ to have the CKEditor_ and TinyMCE_ distributables respectively.
*django-wysiwyg* will automatically find their sources if they are mentioned in the ``INSTALLED_APPS``.

It's also possible to add new editors, see :doc:`extending django-wysiwyg <extending>`


.. _CKEditor: http://ckeditor.com/
.. _Redactor: http://redactorjs.com/
.. _TinyMCE: http://www.tinymce.com/
.. _YAHOO: http://developer.yahoo.com/yui/editor/
.. _django-ckeditor: https://github.com/django-ckeditor/django-ckeditor
.. _django-tinymce: https://github.com/aljosa/django-tinymce
