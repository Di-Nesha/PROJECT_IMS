from django.urls import path
from . import views

urlpatterns = [
    path('',views.quotationrequest_form, name='quotationrequest_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.quotationrequest_form, name='quotationrequest_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.quotationrequest_delete, name='quotationrequest_delete'), # GET & POST request for DELETE operation
    path('list/',views.quotationrequest_list, name='quotationrequest_list') # GET request to retrive and display all records
]