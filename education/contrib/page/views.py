from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('page/home.html', context_instance=RequestContext(request))