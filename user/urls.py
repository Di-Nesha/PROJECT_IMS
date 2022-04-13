from django.urls import path
from . import views

urlpatterns = [

    # path('',views.user_form),
    # path('list/',views.user_list)

    path('',views.user_form, name='user_insert'), # GET & POST request for INSERT operation
    path('<int:id>/',views.user_form, name='user_update'), # GET & POST request for UPDATE operation
    path('delete/<int:id>/',views.user_delete, name='user_delete'), # GET & POST request for DELETE operation
    path('list/',views.user_list, name='user_list') # GET request to retrive and display all records

]
