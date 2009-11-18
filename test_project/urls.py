from django.conf.urls.defaults import *
from django.conf import settings

from views import basic_test

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': settings.MEDIA_ROOT }
        ),
    ('^', basic_test)
)
