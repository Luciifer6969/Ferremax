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
    path('cart/',cart,name='cart'),
    path('cart/add/',agregar_producto,name='agregar'),
    path('productos/',productos,name='productos'),
    path('entrega/',entrega,name='entrega'),
    path('edit_entrega/<int:id_entrega>/',edit_entrega,name='edit_entrega'),
    path('producto/<int:producto_id>/', verProducto, name='verProducto'),
    path('contact/',contact, name='contact'),
]