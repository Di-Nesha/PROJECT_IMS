from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.quotation_form, name='quotation_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.quotation_form, name='quotation_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.quotation_delete, name='quotation_delete'), # GET & POST request for DELETE operation
    path('list/',views.quotation_list, name='quotation_list'), # GET request to retrive and display all records
    path('quotation_pdf', views.quotation_pdf, name='quotation_pdf'),

]