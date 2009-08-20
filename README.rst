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

Handling Content
~~~~~~~~~~~~~~~~

Cleaning HTML
-------------

django_wyswyg.clean_html will be exported if you have either html5lib
(http://code.google.com/p/html5lib/) or pytidylib installed. Both should
install with pip or easy_install, although the later will require having the
htmltidy C library installed.

Using clean_html in views is simple:

    data = django_wyswyg.clean_html(data)

To display raw HTML
-------------------

    {% autoescape off %}
        {{ content }}
    {% endautoescape %}

or

    {{ content|safe }}

*This should not be used without careful consideration if your content comes
from untrusted users*

`clean_html` does not protect against security problems; `sanitize_html`
attempts to do so but is only available with html5lib (tidylib has no
equivalent mode) and should currently be considered experimental.