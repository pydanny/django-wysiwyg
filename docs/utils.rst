=================
Utility functions
=================

Django-wysiwyg provides a few utility functions to deal with HTML from WYSIWYG editors.
Example::

    from django_wysiwyg.utils import clean_html, sanitize_html

    print clean_html("<b><i>test</b></i>")
    print sanitize_html("<b><script>alert(1)</script></b>")


