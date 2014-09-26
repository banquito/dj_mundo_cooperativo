from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^mi_cooperativa/', include('cooperatives.urls')),
)
