import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from egg.models import Egg


def index(request):
    return HttpResponse("Halleluja!")

def egg(request, egg_id):
    e = Egg.objects.get(id=egg_id)
    return render(request, "egg/egg.html", {'e': e})

def hit(request, egg_id):
    e = Egg.objects.get(id=egg_id)
    e.score -= 1
    e.save()
    return HttpResponse(json.dumps({'score': e.score}), content_type='application/json')