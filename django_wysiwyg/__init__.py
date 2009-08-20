def clean_html5lib(input):
    """
    Takes an HTML fragment and processes it using html5lib to ensure that the HTML is well-formed.

    >>> clean_html("<p>Foo<b>bar</b></p>")
    u'<p>Foo<b>bar</b></p>'
    >>> clean_html("<p>Foo<b>bar</b><i>Ooops!</p>")
    u'<p>Foo<b>bar</b><i>Ooops!</i></p>'
    >>> clean_html('<p>Foo<b>bar</b>& oops<a href="#foo&bar">This is a <>link</a></p>')
    u'<p>Foo<b>bar</b>&amp; oops<a href=#foo&amp;bar>This is a &lt;&gt;link</a></p>'
    """
    from html5lib import treebuilders, treewalkers, serializer
    from html5lib.filters import cleanr

    p = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))

    dom_tree = p.parseFragment(input)

    walker = treewalkers.getTreeWalker("dom")

    stream = walker(dom_tree)

    s = serializer.htmlserializer.HTMLSerializer(omit_optional_tags=False, clean=True)
    return "".join(s.serialize(stream))

def sanitize_html5lib(input):
    p = html5lib.HTMLParser(tokenizer=sanitizer.HTMLSanitizer)
    dom_tree = p.parseFragment(input)

    walker = treewalkers.getTreeWalker("dom")

    stream = walker(dom_tree)

    s = serializer.htmlserializer.HTMLSerializer(omit_optional_tags=False, clean=True)
    return "".join(s.serialize(stream))

def clean_pytidylib(input):
    (cleaned_html, warnings) = tidylib.tidy_document(html)
    return cleaned_html

try:
    import html5lib
    clean_html = clean_html5lib
    sanitize_html = sanitize_html5lib
except ImportError:
    try:
        import tidylib
        clean_html = clean_tidylib
    except ImportError:
        pass

if not "clean_html" in locals():
    import logging
    logging.error("Unable to import html5lib or tidylib")
