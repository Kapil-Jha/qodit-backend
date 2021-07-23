# from show import tests
from django.urls import path

from . import views

urlpatterns = [
    path('', views.chooseus,name='ChooseRight'),
    path('<int:pk>/', views.delchooseus,name='ChooseRight'),
   

]