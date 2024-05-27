from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.empleados.models import Empleado
from .models import Departamento 
from .forms import NewDepartmentForm


class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name = 'departamentos'


class NewDepartmentView(FormView):
    template_name = 'departamento/new_department.html'
    form_class = NewDepartmentForm
    success_url = '/'
    
    def form_valid(self, form):
        print('*****************Estamos en el form valid*******************')

        depa = Departamento(
            name=form.cleaned_data['departamento'], 
            shor_name=form.cleaned_data['shorname'], 
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        return super(NewDepartmentView, self).form_valid(form)
    

