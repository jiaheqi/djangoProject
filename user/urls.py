# user文件夹的urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.userLogin, name='userLogin')
]