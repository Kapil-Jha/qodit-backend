
from django.urls import path

from . import views

urlpatterns = [
    path('', views.chooseus,name='chooseleft'),
    path('<int:pk>/', views.delchooseus,name='chooseleft' ),
  

]