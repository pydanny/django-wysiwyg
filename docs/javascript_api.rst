==============
JavaScript API
==============

To support the needs of more advanced web interfaces, django-wysiwyg provides a JavaScript API.
This can be used to enable or disable WYSIWYG editors on demand,
for example, because the element was inserted dynamically though DOM manipulation.

Every editor type provides the following JavaScript functions:

* ``django_wysiwyg.is_loaded()`` - Whether the external scripts for the editor are loaded.
  This can be useful for offline-mode, to refrain from updating textarea fields.
* ``django_wysiwyg.enable(editor_name, field_name)``  - Enable an editor for a given field.
* ``django_wysiwyg.disable(editor_name)`` - Disable the editor.
* ``django_wysiwyg.editors[editor_name]`` - Access to the editor object (e.g. the CKEditor, or YUI Editor object).

---------------------------------
Moving WYSIWYG editors in the DOM
---------------------------------

Most WYSIWYG editors are not built for being moved around in the DOM,
and keep referring to old elements in the event handlers.
A solution to this problem, is disabling  the editor first (which removes all WYSIWYG nodes),
and enable it again after moving the containr.
