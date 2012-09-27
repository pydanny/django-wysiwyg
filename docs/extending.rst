========================
Extending django-wysiwyg
========================

The django-wysiwyg module can easily by extended with new editor types.

The editor switching in implemented by selecting templates based on the ``DJANGO_WYSIWYG_FLAVOR`` setting.
Adding an extra editor simply requires these templates to be added:

* django_wysiwyg/*editorname*/includes.html
* django_wysiwyg/*editorname*/editor_instance.html

-------------
includes.html
-------------

The includes file will be added to the top of the page, to provide all required scripts.
It is loaded by the ``{% wysiwyg_setup %}`` code. The template could contain something like::

    <script type="text/javascript" src="{{ DJANGO_WYSIWYG_MEDIA_URL }}editor.js"></script>
    <script type="text/javascript" src="{{ DJANGO_WYSIWYG_MEDIA_URL }}sample.css"></script>

Secondly, the file has to provide a few JavaScript functions, to implement the :doc:`javascript_api`
This is used for Ajax environments, or interfaces which use a lot of DOM manipulation.
The required API functions have the following structure::

    var django_wysiwyg_editor_configs = [];   // allow custom settings per editor ID{% block django_wysiwyg_editor_config %}
    var django_wysiwyg_editor_config = {};
    {% endblock %}


    var django_wysiwyg =
    {
        editors: {},  // where the editor object can be stored.

        is_loaded: function()
        {
            // ... some test to see if the scripts were loaded properly.
            return window.MY_EDITOR != null;
        },

        enable: function(editor_name, field_name, config)
        {
            if( !config ) {
                config = django_wysiwyg_editor_configs[field_id] || django_wysiwyg_editor_config;
            }

            if( !this.editors[editor_name] ) {
                this.editors[editor_name] = // ... enable the editor for the field name
            }
        },

        disable: function(editor_name)
        {
            var editor = this.editors[editor_name];
            if( editor ) {
                editor.the_destroy_function();   // ... call the destroy function
                this.editors[editor_name] = null;
            }
        }
    }

The ``enable()`` function should be able to deal with attempts to enable the editor twice.
It should also store the created WYSIWYG editor instance in the ``this.editors[editor_name]`` variable.
That allows the caller to access the object when it needs to.

For more inspiration, you can inspect the files in the ``django_wysiwyg`` template directory.

--------------------
editor_instance.html
--------------------

The editor-instance template is used to instantiate a single editor statically.
It is loaded by the ``{% wysiwyg_editor fieldname %}`` line in the template.
The contents of the template can look something like:

::

    <script type="text/javascript">
        (function(){
            var config = {{ config }};
            django_wysiwyg.enable('{{ editor_name }}', '{{ field_id }}', config);
        })();
    </script>

In most cases, this should be enough to instantiate the editor for a specific field.

----------------------------
Extending existing templates
----------------------------

Some templates also provide blocks, that allow them to be extended.
For example, the *yui_advanced* editor, is implemented by extending the *yui* templates.

