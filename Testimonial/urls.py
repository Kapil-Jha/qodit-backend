from django.urls import path

from .import views

urlpatterns = [
    path('', views.qodittesti,name='Testimonials'),
   path('<int:pk>/', views.delqodittesti,name='Testimonials'),
]