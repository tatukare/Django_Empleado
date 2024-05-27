from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(), 
        name='inicio'
    ),
    path(
        'listar-todo-empleados/', 
        views.ListaAllEmpleados.as_view(),
        name='empleados_all'
    ),
    path(
        'lista-by-area/<shorname>', 
        views.ListaByAreaEmpleados.as_view(),
        name='empleados_area'
    ),
    path(
        'lista-empleados_admin', 
        views.ListaEmpleadosAdmin.as_view(),
        name='empleados_admin'
    ),
    path('lista-by-job/<job>', views.ListaByJobEmpleados.as_view()),
    path('buscar-emplado/', views.ListaEmpleadosbyKword.as_view()),
    path('lista-habilidades-empleado/', views.ListHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='empleado_add'
    ),
    path(
        'success/',
        views.SuccesView.as_view(), 
        name='correcto'
    ), 
    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'
    ), 
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'
    ), 
]

