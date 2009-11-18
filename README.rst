DJANGO WYSIWYG
==================

.. contents:: Table of Contents

A Django application for easily converting HTML <textarea>s into rich HTML editors that meet US Government 508/WAC standards. This application has been demonstrated to work just fine with django-uni-form (http://github.com/pydanny/django-uni-form).

Currently this works as a template tag. We did it this way because control of how editing works is arguably a template issue (i.e. presentation) and not a forms/model issue (i.e. control).

We considered other options such as TinyMCE, FCKeditor, various jquery tools and other tools but settled on YUI. We did so because of familiarity and because it meant we don't have to host files locally (you can change that if you want for your own local install and we do that for our own work projects).

If you want to contribute to django-wysiwyg, please do so from the repository at http://github.com/pydanny/django-wysiwyg.

Installation
~~~~~~~~~~~~~~~~

Via pip::

  easy_install django-wysiwyg

Via easy_setup::

  pip install django-wysiwyg

Configuration
~~~~~~~~~~~~~~

Add `'django_wysiwyg'` to your `INSTALLED_APPS` in `settings.py`::

    INSTALLED_APPS = (
        ...
        'django_wysiwyg',
    )

Usage
~~~~~~

Within your pages
-----------------

::

    {% load wysiwyg %}

    {% wysiwyg_setup %}

    <textarea id="foo">

    </textarea>

    {% wysiwyg_editor "my_text_area_id" %}

Within Django Admin
-------------------

django-wyswiyg comes with a custom file that serves as a base template for alterations to admin displays. To make an admin field display rich text, do the following:

#. In your custom app's admin.py file, on the MyModelAdmin class, add ``change_form_template = 'my_app/change_form.html'``. For example::

    from django.contrib import admin
    from pydanny.models import Cartwheel

    class CartWheelAdmin(admin.ModelAdmin):
        change_form_template = 'pydanny/change_form.html'
        
    admin.site.register(Cartwheel, CartwheelAdmin)        

#. copy ``django_wysiwyg/templates/admin/change_form.html`` to  ``my_app/templates/my_app/change_form.html``. For example::

    cp django_wysiwyg/templates/admin/change_form.html pydanny/templates/pydanny/change_form.html
  
#. Now open the new ``my_app/templates/my_app/change_form.html`` file. You will need to set the fields you want made into rich text editors by adding {% wysiwyg_editor "id_description" %} template tag calls. For example::

    {% extends "admin/change_form.html" %}

    {% load wysiwyg %}

    {% block extrahead %}
        {{ block.super }}
        {% wysiwyg_setup %}
        {% wysiwyg_editor "id_description" %}    
    {% endblock %}



----

Handling Content
~~~~~~~~~~~~~~~~

Cleaning HTML
-------------

django_wyswyg.clean_html will be exported if you have either html5lib
(http://code.google.com/p/html5lib/) or pytidylib installed. Both should
install with pip or easy_install, although the later will require having the
htmltidy C library installed.

Using clean_html in views is simple::

    data = django_wyswyg.clean_html(data)

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
