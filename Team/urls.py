from django.urls import path

from .import views

urlpatterns = [
    path('', views.qoditteam),
    path('<int:pk>/', views.delqoditteam),
   


]