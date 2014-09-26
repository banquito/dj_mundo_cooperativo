from django.conf.urls import patterns, url

from cooperatives import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^nombre', views.nombre, name='nombre'),
    url(r'^miembros', views.miembros, name='miembros'),
    url(r'^objeto', views.objeto, name='objeto'),
    url(r'^lugar', views.lugar, name='lugar'),
    url(r'^formacion', views.formacion, name='formacion'),
    url(r'^convocatoria', views.convocatoria, name='convocatoria'),
    url(r'^asamblea', views.asamblea, name='asamblea'),
    url(r'^acta_consejo', views.actaConsejo, name='acta_consejo'),
    url(r'^capital', views.capital, name='capital'),
    url(r'^tramite', views.tramite, name='tramite'),
)