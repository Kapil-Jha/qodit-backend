from django.urls import path

from . import views

urlpatterns = [
    path('', views.qoditfeat, name='Features' ),
    path('<int:pk>/', views.delqoditfeat, name='Features'),
  

]