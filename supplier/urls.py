from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.supplier_form, name='supplier_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.supplier_form, name='supplier_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.supplier_delete, name='supplier_delete'), # GET & POST request for DELETE operation
    path('list/',views.supplier_list, name='supplier_list') # GET request to retrive and display all records
]