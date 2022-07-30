from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inmueblesListApp.api.views import *

router= DefaultRouter()
router.register('empresa', EmpresaVs, basename='empresa')

urlpatterns = [
   
    path('edificacion/', EdificacionListAv.as_view(),name='list'),
    path('detallesi/<int:pk>', EdificacionDetalleAv.as_view(),name='detalle'),
    
    #path('empresa/', EmpresaListAv.as_view(),name='listE'),
    #path('detallese/<int:pk>', EmpresaDetalleAv.as_view(),name='detalleE'),
    path('', include(router.urls)),
    
    path('comentario-create/<int:pk>', ComentarioCreate.as_view(),name='comentario-create'),
    #trae la lista de comentarios pertenecientes a un inmueble
    path('comentario-list/<int:pk>', ComentarioLis.as_view(),name='comentario-list'),
    path('comentario-details/<int:pk>', ComentariosDetail.as_view(),name='comentario-detail'),
]