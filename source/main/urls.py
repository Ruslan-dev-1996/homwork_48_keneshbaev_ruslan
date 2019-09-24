"""main URL Configuration

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
from django.contrib import admin
from django.urls import path
from webapp.views import index_view, detailed_view, form_storage_view, detailed_update_view, detailed_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('detailed/<int:pk>/', detailed_view, name='detailed'),
    path('form/add/', form_storage_view, name='form_storage'),
    path('detailed/<int:pk>/edit/', detailed_update_view, name='update'),
    path('deatiled/<int:pk>/delete/', detailed_delete_view, name='delete')
]
