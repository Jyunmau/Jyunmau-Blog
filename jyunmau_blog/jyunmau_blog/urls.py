"""jyunmau_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import url
from blog_app import views

from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_index),
    re_path(r'article/(\d{1,})/', views.article),
    re_path(r'^article_list/([\u4E00-\u9FA5A-Za-z0-9_]+)/$', views.article_list_cate),
    path('index/', views.blog_index),
    path('article_list/', views.article_list),
]
