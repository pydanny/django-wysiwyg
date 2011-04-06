========
Examples
========

Simple template example::

    {% load wysiwyg %}

    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
       "http://www.w3.org/TR/html4/strict.dtd">

    <html lang="en">
    <head>
    	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    	<title>basic_test</title>
        {% wysiwyg_setup  %}
    </head>
    <body>
        <textarea id="my_text">This is some text. Please edit it</textarea>
        {% wysiwyg_editor "my_text" %}
    </body>
    </html>
