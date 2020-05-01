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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

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
    path('backbin/', views.backbin),
    # path('testuser/', crud.create_testuser),
    path('', views.login)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
