from django.conf.urls.defaults import *
from views import basic_test

urlpatterns = patterns('',
    ('^', basic_test)
)
