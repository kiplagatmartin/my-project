from django.urls import path

from . import views

appname = 'shamba'
urlpatterns = [
    path('', views.signup, name='signup'),
    path('items/', views.items, name='items'),
    path('cart/', views.cart, name='cart'),
]
