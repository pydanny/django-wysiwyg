def clean_html():
    raise ImportError("clean_html requires html5lib or pytidylib")

def sanitize_html():
    raise ImportError("sanitize_html requires html5lib")


try:
    import html5lib
    from utils import clean_html5lib as clean_html
    from utils import sanitize_html5lib as sanitize_html
except ImportError:
    try:
        import tidylib
        from utils import clean_tidylib as clean_html
    except ImportError:
        pass