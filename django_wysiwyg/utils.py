#!/usr/bin/env python

def clean_html(*args, **kwargs):
    raise ImportError("clean_html requires html5lib or pytidylib")

def sanitize_html(*args, **kwargs):
    raise ImportError("sanitize_html requires html5lib")

def clean_html5lib(input):
    """
    Takes an HTML fragment and processes it using html5lib to ensure that the HTML is well-formed.

    >>> clean_html5lib("<p>Foo<b>bar</b></p>")
    u'<p>Foo<b>bar</b></p>'
    >>> clean_html5lib("<p>Foo<b>bar</b><i>Ooops!</p>")
    u'<p>Foo<b>bar</b><i>Ooops!</i></p>'
    >>> clean_html5lib('<p>Foo<b>bar</b>& oops<a href="#foo&bar">This is a <>link</a></p>')
    u'<p>Foo<b>bar</b>&amp; oops<a href=#foo&amp;bar>This is a &lt;&gt;link</a></p>'
    """
    from html5lib import treebuilders, treewalkers, serializer, sanitizer

    p = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))

    dom_tree = p.parseFragment(input)

    walker = treewalkers.getTreeWalker("dom")

    stream = walker(dom_tree)

    s = serializer.htmlserializer.HTMLSerializer(omit_optional_tags=False)

    return "".join(s.serialize(stream))

def sanitize_html5lib(input):
    """

    >>> sanitize_html5lib("foobar<p>adf<i></p>abc</i>")
    u'foobar<p>adf<i></i></p><i>abc</i>'
    >>> sanitize_html5lib('foobar<p style="color:red; remove:me; background-image: url(http://example.com/test.php?query_string=bad);">adf<script>alert("Uhoh!")</script><i></p>abc</i>')
    u'foobar<p style="color: red;">adf&lt;script&gt;alert("Uhoh!")&lt;/script&gt;<i></i></p><i>abc</i>'
    """
    from html5lib import treebuilders, treewalkers, serializer, sanitizer

    p = html5lib.HTMLParser(tokenizer=sanitizer.HTMLSanitizer, tree=treebuilders.getTreeBuilder("dom"))
    dom_tree = p.parseFragment(input)

    walker = treewalkers.getTreeWalker("dom")

    stream = walker(dom_tree)

    s = serializer.htmlserializer.HTMLSerializer(omit_optional_tags=False)
    return "".join(s.serialize(stream))

def clean_pytidylib(input):
    (cleaned_html, warnings) = tidylib.tidy_document(html)
    return cleaned_html

try:
    import html5lib
    clean_html,  sanitize_html = clean_html5lib, sanitize_html5lib
except ImportError:
    try:
        import tidylib
        clean_html = clean_tidylib
    except ImportError:
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()