from django.urls import path
from . import views

urlpatterns = [
    path('',views.employee_form, name='employee_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.employee_form, name='employee_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.employee_delete, name='employee_delete'), # GET & POST request for DELETE operation
    path('list/',views.employee_list, name='employee_list'), # GET request to retrive and display all records
    path('genarate_pdf', views.genarate_pdf, name='genarate_pdf')
]