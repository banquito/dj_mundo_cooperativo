from django.forms import ModelForm
from .models import Cooperative
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