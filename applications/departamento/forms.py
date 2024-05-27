from django import forms 

# class NewDepartmentForm(forms.Form):
#     nombre = forms.CharField(max_length=50)
#     apellido = forms.CharField(max_length=50)
#     departamento = forms.CharField(max_length=50)
#     shorname = forms.CharField(max_length=20)


class NewDepartmentForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre del empleado'})
    )
    apellido = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Apellido del empleado'})
    )
    departamento = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre del departamento'})
    )
    shorname = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Short name del departamento'})
    )
 