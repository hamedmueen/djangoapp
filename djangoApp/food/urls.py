from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order, name='order'),
    path('cart/', views.cart, name='cart'),
    path('cart/order/', views.orderpage, name='orderpage'),
    path('order/back/', views.backhome, name='backhome'),
    path('cart/back/', views.backhome, name='backhom')
]