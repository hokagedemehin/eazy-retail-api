"""easyRetailApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, re_path
# from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework import permissions
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# from rest_framework.authentication import TokenAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from django.views.generic import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="Eazy Retail API",
        default_version='v1',
        description="Endpoints for the Eazy Retail API",
        #   terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ibk2k7@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.IsAdminUser,),
    # authentication_classes=(BasicAuthentication,),
    # patterns=public_apis,
    
)


urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

# add static files url
from django.conf import settings

# if settings.DEBUG:
from django.conf.urls.static import static

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "EazyRetail Admin"
admin.site.site_title = "EazyRetail Admin Portal"
admin.site.index_title = "Welcome to EazyRetail Admin Portal"