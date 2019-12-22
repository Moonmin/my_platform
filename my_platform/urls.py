"""my_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user_manage import views

urlpatterns = [
    # 当包括其它 URL 模式时你应该总是使用 include() ， admin.site.urls 是唯一例外。
    # path 参数：1.router 2.view 调用的视图
    #首页，登录跳转至user_manage下的url.py管理
    path('', include('user_manage.urls')),
    path('login', include('user_manage.urls')),

    path('admin/', admin.site.urls),
]
