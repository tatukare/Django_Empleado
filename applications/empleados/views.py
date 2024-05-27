from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

# models
from .models import Empleado

# forms
from .forms import EmpleadoForm

# Create your views here.
class InicioView(TemplateView):
    ''' Vista que carga la página de inicio '''
    template_name = 'inicio.html'


# 1) Lista todos los empleados de la empresa
class ListaAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    paginate_by = 7 
    ordering = 'first_name'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )  
        return lista
    

class ListaEmpleadosAdmin(ListView):
    template_name = 'empleados/lista_empleados.html'
    paginate_by = 7 
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
    


# 2) Listar todos los empleados que pertenecen a un área de la empresa
class ListaByAreaEmpleados(ListView):
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__shor_name = area
        ) 
        return lista
    

# 3) Listar empleados por trabajo
class ListaByJobEmpleados(ListView):
    template_name = 'empleados/list_by_job.html'
    
    def get_queryset(self):
        job = self.kwargs['job']
        lista = Empleado.objects.filter(
            job = job
        ) 
        return lista
       

# 4) listar los empleados por palabra clave
class ListaEmpleadosbyKword(ListView):
    template_name = 'empleados/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('*' * 20 )
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )  
        return lista


# 5) Listar habilidades de un empleado 
class ListHabilidadesEmpleado(ListView):
    template_name = 'empleados/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=8)
        return empleado.habilidades.all()
    

# Detail View 
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleados/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # todo el proceso para verificar empleado del mes
        context['titulo'] = 'Empleado del mes'
        return context


# Create View 
class EmpleadoCreateView(CreateView):
    template_name = "empleados/add.html"
    model = Empleado 
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        print(empleado)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name 
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class SuccesView(TemplateView):
    template_name = "empleados/success.html"  


# Update View
class EmpleadoUpdateView(UpdateView):
    template_name = "empleados/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
     ]
    success_url = reverse_lazy('empleados_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('**************************METODO POST*****************')
        print('===================================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('**************************METODO from_valid*****************')
        print('******************************************************')
        return super(EmpleadoUpdateView, self).form_valid(form)
    

# Delete View 
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleados/delete.html"
    success_url = reverse_lazy('empleados_app:empleados_all')

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = reverse_lazy('empleados_app:correcto')
        self.object.delete()
        return super().post(request, *args, **kwargs)


