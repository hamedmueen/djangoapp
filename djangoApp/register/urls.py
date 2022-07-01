from django.urls import path
from . import views

urlpatterns = [
    path('LoginPage', views.login, name='login')
]