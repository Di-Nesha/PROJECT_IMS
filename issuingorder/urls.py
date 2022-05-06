from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.issuingorder_form, name='issuingorder_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.issuingorder_form, name='issuingorder_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.issuingorder_delete, name='issuingorder_delete'), # GET & POST request for DELETE operation
    path('list/',views.issuingorder_list, name='issuingorder_list') # GET request to retrive and display all records
]