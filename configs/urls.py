"""configs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg2 import openapi  # add swagger
from drf_yasg2.views import get_schema_view  # add swagger
from rest_framework import permissions  # new

Schemaview = get_schema_view(  # add swagger
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="A sample API for learning DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="lamhai1401@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("django.contrib.auth.urls")),  # update user detail
    path("accounts/", include("accounts.urls")),
    path(
        "swagger/",
        Schemaview.with_ui("swagger", cache_timeout=0),  # add swagger
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        Schemaview.with_ui("redoc", cache_timeout=0),  # add swagger
        name="schema-redoc",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
