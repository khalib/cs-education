from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from education.libraries.cse.api import CSEAPI


def view(request, slug):
    api = CSEAPI()
    product = api.get_product_by_slug(slug)

    payload = {
        'product': product,
        'review': product.review,
    }

    # print product.review.author

    return render_to_response('review/view.html', payload, context_instance=RequestContext(request))