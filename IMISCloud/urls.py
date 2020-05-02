"""IMISCloud URL Configuration

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
from django.views import static
from IMISCloud import settings
from cloudApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('upload/', views.upload),
    path('result/', views.searchresult),
    path('recycle/', views.recycle),
    path('update/', views.update),
    path('drop/', views.drop),
    path('delete/', views.delete),
    path('backbin/', views.backbin),
    path('clearsession/', views.clearsession),
    path('register/', views.register),
    path('', views.login)
]

urlpatterns += [re_path(r'^CloudStorage/(?P<path>.*)$', static.serve, {"document_root": settings.MEDIA_ROOT},
                        name='media')]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),
    ]
