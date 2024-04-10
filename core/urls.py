from django.urls import path
from .views import *

urlpatterns = [

    path('',index, name="index"),
    path('auth_register/',auth_register,name='auth_register'),
    path('auth_login/',auth_login,name='auth_login'),
    path('logout/',exit,name='exit'),
]