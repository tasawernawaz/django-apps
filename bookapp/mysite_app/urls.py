from views import hello, current_time, meta_view, contact, thanks

__author__ = 'Tasawer Nawaz'

from django.conf.urls import *


urlpatterns = patterns('',
                       (r'^time/$', current_time),
                        (r'^hello/$', hello),
                        (r'^meta/$',meta_view),
    (r'^contact/$',contact),
    (r'^thanks/$',thanks))

