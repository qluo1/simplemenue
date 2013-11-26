from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
	""" """
	return render_to_response("index.html",
		context_instance=RequestContext(request))

def product(request):
	""" """
	return render_to_response("product.html",
		context_instance=RequestContext(request))

def services(request):
	""" """
	return render_to_response("services.html",
		context_instance=RequestContext(request))

def about(request):
	""" """
	return render_to_response("about.html",
		context_instance=RequestContext(request))

def contact(request):
	""" """
	return render_to_response("contact.html",
		context_instance=RequestContext(request))
