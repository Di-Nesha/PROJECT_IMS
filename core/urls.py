from django.contrib import admin
from django.urls import path
from core import views

app_name = "core" 

urlpatterns = [
 path('admin/', admin.site.urls),
 path('', views.Index.as_view(), name='index'),
 path('login/', views.Login.as_view(), name='login'),
path('401.html', views.Login.as_view(), name='401'),
 path('404/', views.Login.as_view(), name='404'),
 path('500/', views.Login.as_view(), name='500'),

]
