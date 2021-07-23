from django.urls import path

from .import views

urlpatterns = [
   
    path('send/', views. contactsendmail,name='ContactUs'),
    path('delete', views.deleteall,name='ContactUs'),
    path('deletelist/<int:pk>/', views.deletelist,name='ContactUs'),
  

]