from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mi_cooperativa/index.html')

def nombre(request):
    return render(request, 'mi_cooperativa/nombre.html')

def miembros(request):
    return render(request, 'mi_cooperativa/miembros.html')

def objeto(request):
    return render(request, 'mi_cooperativa/objeto.html')

def lugar(request):
    return render(request, 'mi_cooperativa/lugar.html')

def formacion(request):
    return render(request, 'mi_cooperativa/formacion.html')

def convocatoria(request):
    return render(request, 'mi_cooperativa/convocatoria.html')

def asamblea(request):
    return render(request, 'mi_cooperativa/asamblea.html')

def actaConsejo(request):
    return render(request, 'mi_cooperativa/acta_consejo.html')

def capital(request):
    return render(request, 'mi_cooperativa/capital.html')

def tramite(request):
    return render(request, 'mi_cooperativa/tramite.html')
