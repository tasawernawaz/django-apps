__author__ = 'Tasawer Nawaz'


from django.conf.urls import   *
from js.views import hello1, contact_form, search_name

urlpatterns = patterns('',
    (r'^hello1/$',hello1),
    (r'^contact',contact_form),
    (r'^request_result',search_name))