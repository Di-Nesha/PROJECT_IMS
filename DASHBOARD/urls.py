"""DASHBOARD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/',include('employee.urls')),
    path('user/',include('user.urls')),
    path('privilege/',include('privilege.urls')),
    path('supplier/',include('supplier.urls')),
    path('department/',include('department.urls')),
    path('departmentorder/',include('departmentorder.urls')),
    path('issuingorder/',include('issuingorder.urls')),
    path('quotationrequest/',include('quotationrequest.urls')),
    path('item/',include('item.urls')),
    path('inventory/',include('inventory.urls')),
    path('quotation/',include('quotation.urls')),

    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('password/', views.Password.as_view(), name='password'),
]
 