from django.contrib import admin
from django.urls import path, include

from inmueblesListApp.api.views import *

urlpatterns = [
   
    path('list/', InmueblesListAv.as_view(),name='list'),
    path('<int:pk>', InmuebleDetalleAv.as_view(),name='detalle'),
]