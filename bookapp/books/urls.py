from books import views

__author__ = 'Tasawer Nawaz'

from views import add_author
from django.conf.urls import *

urlpatterns =patterns('',
    (r'^add_author/$', add_author),
    (r'^search_book/$',views.search_form_book),
    (r'^search/$',views.search_book))