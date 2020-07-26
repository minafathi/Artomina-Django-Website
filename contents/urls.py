from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path
from . import views

name_app = 'contents'
urlpatterns = [
    path('', views.content_list, name='content_list'),
    path('<int:pk>', views.content_detail, name='content_detail')
]

urlpatterns += staticfiles_urlpatterns()