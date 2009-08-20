DJANGO WYSIWYG
==================

A Django application for easily converting HTML <textarea>s into rich HTML editors.

Currently as a template tag and possibly as a form widget.

At the moment we are using YUI's editor. We are considering other options such as TinyMCE.

Installation
~~~~~~~~~~~~~~~~

    pip install (egg location)

Configuration
~~~~~~~~~~~~~~

Add `'django_wysiyg'` to your `INSTALLED_APPS` in `settings.py`::

    INSTALLED_APPS = (
        ...
        'django_wysiyg',
    )

Usage
~~~~~~

Within your pages
-----------------

    {% load wysiwyg %}

    {% wysiwyg_setup %}

    <textarea id="foo">

    </textarea>

    {% wysiwyg_editor "my_text_area_id" %}

Within Django Admin
-------------------

    Copy `templates/admin/change_form.html` to your template root for the areas
    you want to enable rich editing - e.g. `templates/admin/myapp/mymodel.html`
    - and, if your HTML object is not named "body" adjust the id passed to the
    `wysiwyg_editor` tag (note that Django admin will prefix your field names
    with `id_`).