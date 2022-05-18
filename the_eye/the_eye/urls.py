from django.urls import re_path
from the_eye import views

urlpatterns = [
    re_path(r'^events/$', views.event_list),
    re_path(r'^events/(?P<pk>[0-9]+)/$', views.event_detail),
]