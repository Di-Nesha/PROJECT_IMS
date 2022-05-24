from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.item_form, name='item_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.item_form, name='item_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.item_delete, name='item_delete'), # GET & POST request for DELETE operation
    path('list/',views.item_list, name='item_list') # GET request to retrive and display all records
]