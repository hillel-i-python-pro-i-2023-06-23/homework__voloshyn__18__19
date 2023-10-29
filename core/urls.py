"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from application import views

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API",
    ),
    public=True,
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    path('contacts/', views.view_contacts, name='view-contacts'),
    path('contacts/create/', views.create_contact, name='create-contact'),
    path('contacts/view/<int:pk>/', views.view_contact, name='view-contact'),
    path('contacts/edit/<int:pk>/', views.edit_contact, name='edit-contact'),
    path('contacts/delete/<int:pk>/', views.delete_contact, name='delete-contact'),

]
