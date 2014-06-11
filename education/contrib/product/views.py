from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from education.contrib.product.models import Product


def view(request, slug):
    return render_to_response()