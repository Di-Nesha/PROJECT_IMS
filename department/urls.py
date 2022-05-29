from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.department_form, name='department_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.department_form, name='department_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.department_delete, name='department_delete'), # GET & POST request for DELETE operation
    path('list/',views.department_list, name='department_list'), # GET request to retrive and display all records
    path('department_pdf', views.department_pdf, name='department_pdf')

]