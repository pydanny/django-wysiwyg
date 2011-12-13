from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from views import basic_test

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': settings.MEDIA_ROOT }
        ),
    ('^$', basic_test),
    url(r"^admin/", include(admin.site.urls)),    
)
