from django.urls import re_path, path,include
from todolistApp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    re_path(r'^staff/$', views.staff_api, name='staff_api'),
    re_path(r'^staff/(?P<staff_id>[0-9]+)$', views.staff_api, name='staff_detail'),
    re_path(r'^tasksPro/$', views.tasksPro_api, name='tasksPro_api'),
    re_path(r'^tasksPro/(?P<id>[0-9]+)$', views.tasksPro_api, name='tasksPro_detail'),
    re_path(r'^tasksPers/$', views.tasksPers_api, name='tasksPers_api'),
    re_path(r'^tasksPers/(?P<id>[0-9]+)$', views.tasksPers_api, name='tasksPers_detail'),
    re_path(r'^projects/$', views.projects_api, name='projects_api'),
    re_path(r'^projects/(?P<id>[0-9]+)$', views.projects_api, name='projects_detail'),
    re_path(r'^comptes/$', views.comptes_api, name='comptes_api'),
    re_path(r'^comptes/(?P<id>[0-9]+)$', views.comptes_api, name='comptes_detail'),
    re_path(r'^save_file/$', views.save_file, name='save_file'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)