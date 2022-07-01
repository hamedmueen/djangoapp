from django.urls import path
from . import views

urlpatterns = [
    path('', views.openPage, name='openPage'),
    path('register', views.registerPage, name='registerPage'),
    path('login', views.loginPage, name='loginPage')
]