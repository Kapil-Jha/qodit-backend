# from show import tests
from django.urls import path

from . import views
import Navbar

urlpatterns = [
    path('', views.showqodit,name='Navbar'),
    path('<int:pk>/', views.qodit,name='Navbar'),
  
]

