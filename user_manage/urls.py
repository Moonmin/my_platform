from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),  # 首页
    path('login', views.user_login)  # 登录
]
