from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from education.libraries.cse.api import CSEAPI

def view(request, id):
    api = CSEAPI()
    product = api.get_product(id)

    return render_to_response('product/view.html', dict(product=product), context_instance=RequestContext(request))