__author__ = 'Daniel Greenfeld, Chris Adams'

VERSION = (0, 5, 0)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    return version

__version__ = get_version()

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