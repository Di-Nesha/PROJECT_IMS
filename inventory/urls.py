from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.inventory_form, name='inventory_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.inventory_form, name='inventory_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.inventory_delete, name='inventory_delete'), # GET & POST request for DELETE operation
    path('list/',views.inventory_list, name='inventory_list'), # GET request to retrive and display all records
    path('inventory_pdf', views.inventory_pdf, name='inventory_pdf'),

]