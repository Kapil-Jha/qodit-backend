from django.urls import path

from .import views

urlpatterns = [
    path('', views.qodithero,name='HeroBox'),
    path('<int:pk>/', views.delqodithero,name='HeroBox'),
    

]