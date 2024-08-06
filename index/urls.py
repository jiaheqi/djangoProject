# index的urls.py
from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.index.as_view(), name='index'),
    # path('<pk>.html',views.index.as_view(),name = 'index'),
    path('result', views.result, name='result'),
    # path('<age>.html',views.index.as_view(),name = 'index'),
    # 添加带有字符类型、整型和slug的路由
    path('<year>/<int:month>/<slug:day>', views.myvariable, name='myvariable'),
    # 添加路由地址外的变量
    # path('', views.index, {'month': '2024/07/24'}),
    # 正则路由定义
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate),
    # 路由重定向
    # path('turnTo', RedirectView.as_view(url='/'), name='turnTo'),
    path('turnTo', views.turnTo.as_view(), name='turnTo'),
    path('download/file1', views.download_file1, name='download_file1'),
    path('download/file2', views.download_file2, name='download_file2'),
    path('download/file3', views.download_file3, name='download_file3'),
    # path('', views.upload, name='upload')
    path('create', views.create, name='create'),
    path('myCookie', views.myCookie, name='myCookie'),
    path('getHeader', views.getHeader, name='getHeader'),
    # path('', views.indexView, name='index')

]
