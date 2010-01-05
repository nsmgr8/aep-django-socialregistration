from django.conf.urls.defaults import *

rootpatterns = patterns('',
    (r'^social/account/', include('socialregistration.urls')),
)
