from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Cooperative, Partner
from .forms import CooperativeNombreForm, CooperativeObjetoForm, CooperativeLugarForm

def index(request):
    cooperatives = Cooperative.objects.all()
    return render(request, 'mi_cooperativa/index.html', {'cooperatives':cooperatives})

def detail(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)
    return render(request, 'mi_cooperativa/detail.html', {'cooperative':cooperative} )

def nombre(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)

    if request.POST:
        f = CooperativeNombreForm(request.POST, instance=cooperative)
        f.save()
        return HttpResponseRedirect(reverse('detail', args=(cooperative_id,)))

    return render(request, 'mi_cooperativa/nombre.html', {'cooperative':cooperative})

def miembros(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)
    partners = Partner.objects.all()

    if request.POST:
        f = CooperativeMiembroForm(request.POST, instance=cooperative)
        f.save()
        return HttpResponseRedirect(reverse('detail', args=(cooperative_id,)))

    return render(request, 'mi_cooperativa/miembros.html', {'cooperative':cooperative, 'partners':partners})

def objeto(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)

    if request.POST:
        f = CooperativeObjetoForm(request.POST, instance=cooperative)
        f.save()
        return HttpResponseRedirect(reverse('detail', args=(cooperative_id,)))

    return render(request, 'mi_cooperativa/objeto.html', {'cooperative':cooperative})

def lugar(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)

    if request.POST:
        f = CooperativeLugarForm(request.POST, instance=cooperative)
        f.save()
        return HttpResponseRedirect(reverse('detail', args=(cooperative_id,)))

    form = CooperativeLugarForm(instance=cooperative)
    return render(request, 'mi_cooperativa/lugar.html', {'cooperative':cooperative, 'form':form })

def formacion(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)
    return render(request, 'mi_cooperativa/formacion.html', {'cooperative':cooperative})

def convocatoria(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)
    return render(request, 'mi_cooperativa/convocatoria.html', {'cooperative':cooperative})

def asamblea(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)
    return render(request, 'mi_cooperativa/asamblea.html', {'cooperative':cooperative})

def actaConsejo(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)
    return render(request, 'mi_cooperativa/acta_consejo.html', {'cooperative':cooperative})

def capital(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)
    return render(request, 'mi_cooperativa/capital.html', {'cooperative':cooperative})

def tramite(request, cooperative_id):
    cooperative = get_object_or_404(Cooperative, pk=cooperative_id)
    return render(request, 'mi_cooperativa/tramite.html', {'cooperative':cooperative})
