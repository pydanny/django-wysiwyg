from setuptools import setup, find_packages

version = '0.4.1'

LONG_DESCRIPTION = """
DJANGO WYSIWYG
==================

.. contents:: Table of Contents

A Django application for easily converting HTML <textarea>s into rich HTML
editors that meet US Government 508/WAC standards. This application has been
demonstrated to work just fine with django-uni-form
(http://github.com/pydanny/django-uni-form).

Currently this works as a template tag. We did it this way because control of
how editing works is arguably a template issue (i.e. presentation) and not a
forms/model issue (i.e. control).

YUI is the default editor due to familiarity, accessiblity and the fact that
it's possible to run with entirely off of Yahoo's CDN, avoiding the need to
maintain any local resources. CKEditor can be used but will require you to
install the CKEditor files in STATIC_URL/ckeditor (see below).

If you want to contribute to django-wysiwyg, please do so from the repository
at http://github.com/pydanny/django-wysiwyg.

**Note**: This may be obvious, but this only works on ``<textarea>`` (models.TextField) and not simple character ( ``<input>`` ) fields.

Installation
~~~~~~~~~~~~~~~~

Via pip::

  pip install django-wysiwyg

Configuration
~~~~~~~~~~~~~~

Add `'django_wysiwyg'` to your `INSTALLED_APPS` in `settings.py`::

    INSTALLED_APPS = (
        ...
        'django_wysiwyg',
    )

If you wish to use CKEditor set the flavor in `settings.py`::

    DJANGO_WYSIWYG_FLAVOR = "ckeditor"

Please note that doing so requires you to either place the ckeditor
distributables under `STATIC_URL/ckeditor` or set `DJANGO_WYSIWYG_MEDIA_URL`
in `settings.py` to the appropriate location containing the ckeditor
distribution.

Usage
~~~~~~

Within your pages
-----------------

There are two template tags: ``wysiwyg_setup`` must be called once per page,
preferably in the <head>, to load the JavaScript dependencies.
``wysiwyg_editor`` should be called once per text area, after the text area has
been created. A simple example::

    {% load wysiwyg %}
    {% wysiwyg_setup %}

    <textarea id="foo"></textarea>

    {% wysiwyg_editor "foo" %}

Within Django Admin
-------------------

django-wysiwyg comes with a custom file that serves as a base template for
alterations to admin displays. To make an admin field display rich text, do
the following:

#. In your custom app's admin.py file, on the MyModelAdmin class, add
   ``change_form_template = 'my-app-name/admin/change_form.html'``. For example::

    from django.contrib import admin
    from fun.models import Playground

    class PlaygroundAdmin(admin.ModelAdmin):
        change_form_template = 'fun/admin/change_form.html'

    admin.site.register(admin, PlaygroundAdmin)

#. copy ``django_wysiwyg/templates/my-app-name/admin/change_form.html`` to  ``my_app/templates/<my-app-name>/adminchange_form.html``. For example::

    cp django_wysiwyg/templates/admin/my-app-name/change_form.html pydanny/templates/fun/admin/change_form.html

#. Now open the new ``pydanny/templates/my-app-name/admin/change_form.html`` file. You
   will need to set the fields you want made into rich text editors by adding
   {% wysiwyg_editor "id_description" %} template tag calls, replacing
   "id_description" with whatever your form's HTML field is named. For
   example::

    {% extends "admin/change_form.html" %}

    {% load wysiwyg %}

    {% block extrahead %}
        {{ block.super }}
        {% wysiwyg_setup %}
    {% endblock %}

    {% block content %}
        {{ block.super }}
        {% wysiwyg_editor "id_description" %}
    {% endblock %}

----

Handling Content
~~~~~~~~~~~~~~~~

Cleaning HTML
-------------

django_wysiwyg.clean_html will be exported if you have either html5lib
(http://code.google.com/p/html5lib/) or pytidylib installed. Both should
install with pip or easy_install, although the later will require having the
htmltidy C library installed.

Using clean_html in views is simple::

    data = django_wysiwyg.clean_html(data)

To display raw HTML
-------------------

In your templates::

    {% autoescape off %}
        {{ content }}
    {% endautoescape %}

or::

    {{ content|safe }}

*This should not be used without careful consideration if your content comes
from untrusted users*

`clean_html` does not protect against security problems; `sanitize_html`
attempts to do so but is only available with html5lib (tidylib has no
equivalent mode) and should currently be considered experimental.


"""

setup(
    name='django-wysiwyg',
    version=version,
    description="django-wysiwyg",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django',
    author='Daniel Greenfeld, Chris Adams',
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/django-wysiwyg',
    license='MIT',
    packages=find_packages(exclude=('test_project',)),
    include_package_data=True,
    zip_safe=False
)
