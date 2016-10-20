from django.shortcuts import render_to_response
from django.template import RequestContext

def base_view(request):
	return render_to_response('base.html', context_instance = RequestContext(request))

def index_view (request):	
	return render_to_response('home/index.html', context_instance = RequestContext(request))

# Create your views here.
