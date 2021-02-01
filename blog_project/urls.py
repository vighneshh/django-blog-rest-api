"""blog_project URL Configuration

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
from django.urls import path, include,re_path
# from rest_framework.documentation import include_docs_urls # new
# from rest_framework.schemas import get_schema_view # new

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# API_TITLE = 'Blog API' # new
# API_DESCRIPTION = 'A Web API for creating and editing blog posts.' # new
# schema_view = get_schema_view(title=API_TITLE) # new


schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="A Web API for creating and editing blog posts.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')), # new
    path('api-auth/', include('rest_framework.urls')), # new
    path('api/v1/rest-auth/', include('rest_auth.urls')), # new
    path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')), #new
    path('accounts/', include('allauth.urls')),
#     path('docs/', include_docs_urls(title=API_TITLE,
# description=API_DESCRIPTION)), # new
#     path('schema/', schema_view), # new
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    
]


