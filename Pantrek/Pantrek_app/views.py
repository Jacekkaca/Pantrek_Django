from django.shortcuts import render
from django.conf import settings
from django.template.context import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def menu(request):
    return render_to_response("menu.html", {
    }, context_instance=RequestContext(request))

def company(request):
    return render_to_response("company.html", {
    }, context_instance=RequestContext(request))

def trip_summary(request):
    return render_to_response("trip_summary.html", {
    }, context_instance=RequestContext(request))

def seat(request):
    return render_to_response("seat.html", {
    }, context_instance=RequestContext(request))

def search_results(request):
    return render_to_response("search_results.html", {
    }, context_instance=RequestContext(request))

def confirmation(request):
    return render_to_response("confirmation.html", {
    }, context_instance=RequestContext(request))

def home(request):
    return render_to_response("index.html", {
    }, context_instance=RequestContext(request))
