"""
URL configuration for Table_Chemistry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include, re_path
from rest_framework import routers
from elementos.views import ElementoViewSet
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from elementos.views import ShortElementoViewSet


#router = routers.DefaultRouter()
#router.register(r'elementos', ElementoViewSet)
#router.register(r'short_elementos', ShortElementoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/elementos/', ElementoViewSet.as_view({'get': 'list'}), name='elementos-list'),
    path('api/short_elementos/', ShortElementoViewSet.as_view({'get': 'list'}), name='short-elementos-list'),
]

