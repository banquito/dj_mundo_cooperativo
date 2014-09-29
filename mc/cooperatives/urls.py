from django.conf.urls import patterns, url

from cooperatives import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cooperative_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<cooperative_id>\d+)/nombre', views.nombre, name='nombre'),
    url(r'^(?P<cooperative_id>\d+)/miembros', views.miembros, name='miembros'),
    url(r'^(?P<cooperative_id>\d+)/objeto', views.objeto, name='objeto'),
    url(r'^(?P<cooperative_id>\d+)/lugar', views.lugar, name='lugar'),
    url(r'^(?P<cooperative_id>\d+)/formacion', views.formacion, name='formacion'),
    url(r'^(?P<cooperative_id>\d+)/convocatoria', views.convocatoria, name='convocatoria'),
    url(r'^(?P<cooperative_id>\d+)/asamblea', views.asamblea, name='asamblea'),
    url(r'^(?P<cooperative_id>\d+)/acta_consejo', views.actaConsejo, name='acta_consejo'),
    url(r'^(?P<cooperative_id>\d+)/capital', views.capital, name='capital'),
    url(r'^(?P<cooperative_id>\d+)/tramite', views.tramite, name='tramite'),
)