"""{{cookiecutter.project_slug}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView ,TokenVerifyView




urlpatterns = [
    path(
        'api/{{cookiecutter.project_slug}}/users/',
        include('apps.users.urls')
    ),
    path(
        'api/{{cookiecutter.project_slug}}/token/',
        TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'
    ),
    path(
        'api/token/verify/',
         TokenVerifyView.as_view(), name='token_verify'
    ),
    path(
        'api/{{cookiecutter.project_slug}}/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'api/{{cookiecutter.project_slug}}/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
]



urlpatterns = format_suffix_patterns(urlpatterns)
