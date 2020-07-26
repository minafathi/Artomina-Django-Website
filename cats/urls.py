from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path
from . import views

name_app = 'cats'
urlpatterns = [
    path('',views.cat_list, name='cat_list'),
    path('<int:cat_pk>/<int:paint_pk>/', views.paint_detail, name='paint'),
    path('<int:pk>', views.cat_detail, name="detail"),
    path('album/', views.paint_list, name="album"),
]

urlpatterns += staticfiles_urlpatterns()