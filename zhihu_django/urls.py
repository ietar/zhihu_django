"""zhihu_django URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from personal import views
from zhihu_django import settings

urlpatterns = [
    re_path('^$', views.index),
    path('admin/', admin.site.urls),
    re_path('personal/', include('personal.urls')),
    re_path('index1/$', views.index1),
    re_path('shit/$', views.shit),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
