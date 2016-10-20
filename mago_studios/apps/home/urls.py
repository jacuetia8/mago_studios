from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mago_studios.apps.home.views',
	url(r'^$', 'index_view', name = 'vista_index'),
	
)
