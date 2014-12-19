from django.forms import ModelForm, TextInput
from .models import Cooperative, Partner

from django import forms
from django.forms.extras.widgets import SelectDateWidget

class CooperativeNombreForm(ModelForm):
    class Meta:
        model = Cooperative
        fields = ['nombre', 'descripcion']

class CooperativeObjetoForm(ModelForm):
    class Meta:
        model = Cooperative
        fields = ['objeto']

class CooperativeLugarForm(ModelForm):
    class Meta:
        model = Cooperative
        fields = ['direccion', 'localidad', 'provincia', 'codigo_postal']

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')

class CooperativeMiembroForm(ModelForm):
    class Meta:
        model = Partner
        fields = [
            'cooperative', 
            'nombre', 
            'apellido', 
            'correo_electronico', 
            'direccion', 
            'localidad',
            'dni',
            'fecha_de_nacimiento',
        ]
        widgets = {
            'fecha_de_nacimiento': TextInput(attrs={'type': 'date'})
        }
