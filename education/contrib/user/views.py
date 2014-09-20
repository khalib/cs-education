from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from education.libraries.cse.api import CSEAPI


def view(request, slug):
    api = CSEAPI()
    user = api.get_user_by_slug(slug)
    flows = api.get_nodes('flow', { 'author_id': user.id, 'status': 1 })
    boards = api.get_nodes('board', { 'author_id': user.id, 'status': 1 })

    payload = {
        'user': user,
        'flows': flows,
        'boards': boards,
    }

    return render_to_response('user/view.html', payload, context_instance=RequestContext(request))