from django.contrib import admin
from django.urls import path

from . import views

app_name = 'departamento_app'

urlpatterns = [
    path(
        'DepartamentoListView/', 
        views.DepartamentoListView.as_view(), 
        name='departamento_list'
    ),
    path('new-department/', views.NewDepartmentView.as_view(), name='nuevo_departamento'),
]
