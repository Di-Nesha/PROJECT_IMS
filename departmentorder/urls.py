from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.departmentorder_form, name='departmentorder_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.departmentorder_form, name='departmentorder_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.departmentorder_delete, name='departmentorder_delete'), # GET & POST request for DELETE operation
    path('list/',views.departmentorder_list, name='departmentorder_list') # GET request to retrive and display all records
]