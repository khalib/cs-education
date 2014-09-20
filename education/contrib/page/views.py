from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from education.libraries.cse.api import CSEAPI

def home(request):
    api = CSEAPI()
    products = api.get_products()

    return render_to_response('page/home.html', dict(products=products), context_instance=RequestContext(request))