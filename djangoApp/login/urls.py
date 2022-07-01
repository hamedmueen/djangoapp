from django.urls import path
from . import views

urlpatterns = [
    path('failedlogin/', views.failedlogin, name='failedlogin'),
    path('failedlogin/backtologin/', views.backtologin, name='backtologin'),
    path('home', views.home, name='home'),
    path('home/<int:id>/', views.addtocart, name='addtocart'),
    path('loggedout/', views.signout, name='signout'),
    path('back/', views.backhome, name='backhome'),
    path('cart/<str:name>/', views.removeitem, name='removeitem')
]