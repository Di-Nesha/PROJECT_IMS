from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.privilege_form, name='privilege_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.privilege_form, name='privilege_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.privilege_delete, name='privilege_delete'), # GET & POST request for DELETE operation
    path('list/',views.privilege_list, name='privilege_list') # GET request to retrive and display all records
]