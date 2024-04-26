from django.urls import path
from .views import *

urlpatterns = [

    path('',index, name="index"),
    path('auth_register/',auth_register,name='auth_register'),
    path('auth_login/',auth_login,name='auth_login'),
    path('logout/',exit,name='exit'),
    path('stock_products/',stock_products,name='stock'),
    path('pedidos/',pedidos,name='pedidos'),
    path('solicitud_bodega/',solicitud_bodega,name='solicitudes'),
]