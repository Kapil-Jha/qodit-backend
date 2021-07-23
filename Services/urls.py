from django.urls import path

from .import views

urlpatterns = [
    path('', views.qoditserv,name='Services'),
   path('<int:pk>/', views.delqoditserv,name='Services'),
    


]