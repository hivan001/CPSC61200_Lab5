from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader


def index(request):
    template = loader.get_template('helloWorld.html')

    return HttpResponse(template.render())


def json(request):
    return JsonResponse({'Message':'Hello World'})

