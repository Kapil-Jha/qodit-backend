from django.urls import path

from .import views

urlpatterns = [
    path('', views.qoditus,name='AboutUs'),
    path('<int:pk>/', views.delqoditus,name='AboutUs'),
 
 
]
