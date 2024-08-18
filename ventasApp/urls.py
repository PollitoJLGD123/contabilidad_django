from django.urls import path,include 
from ventasApp.views import (
    listarcategoria, agregarcategoria, editarcategoria, eliminarcategoria,
    listar_clientes, crear_cliente, editar_cliente, eliminar_cliente,
    listar_unidades, agregar_unidades, eliminar_unidades, editar_unidades,
    listar_productos, crear_producto, editar_producto, eliminar_producto,
    listar_ventas, crear_venta, editar_venta, eliminar_venta, get_cliente_documento,reporte_pdf,
    cuadro_mando_integral
)
from django.contrib.auth import views

urlpatterns = [ 
    path('listacategoria/',listarcategoria,name="listarcategoria"), 
    path('agregarcategoria/',agregarcategoria ,name="agregarcategoria"),
    path('editarcategoria/<int:id>/',editarcategoria ,name="editarcategoria"),
    path('eliminarcategoria/<int:id>/',eliminarcategoria,name="eliminarcategoria"), 
    
    path('listar_unidades/',listar_unidades,name="listar_unidades"), 
    path('agregar_unidades/',agregar_unidades,name="agregar_unidades"),
    path('editar_unidades/<int:id>/',editar_unidades,name="editar_unidades"),
    path('eliminar_unidades/<int:id>/',eliminar_unidades,name="eliminar_unidades"),  
    
    path('clientes/', listar_clientes, name='listar_clientes'),
    path('clientes/crear/', crear_cliente, name='crear_cliente'),
    path('clientes/editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:id>/', eliminar_cliente, name='eliminar_cliente'),
    
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/editar/<int:id>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', eliminar_producto, name='eliminar_producto'),
    
    path('ventas/', listar_ventas, name='listar_ventas'),
    path('ventas/crear/', crear_venta, name='crear_venta'),
    path('ventas/editar/<int:venta_id>/', editar_venta, name='editar_venta'),
    path('ventas/eliminar/<int:venta_id>/', eliminar_venta, name='eliminar_venta'),
    
    path('get-cliente-documento/<int:cliente_id>/', get_cliente_documento, name='get_cliente_documento'),
    
    
    path('reportepdf/<int:id>', reporte_pdf, name='reporte_pdf'),
    

    path('cuadro_integral', cuadro_mando_integral, name='cuadro_integral'),
    
    ]


