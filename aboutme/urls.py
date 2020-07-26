from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path
from . import views

name_app = 'aboutme'
urlpatterns = [
    path('', views.me, name='aboutme'),
]
