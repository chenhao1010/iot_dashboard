from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Sensors


def info(request):
    return HttpResponse("CREATED BY SAM MIRKAZEMI (sammirkazemi@outlook.com)")


def paho(request):
    template = loader.get_template('paho/index.html')
    return HttpResponse(template.render({}, request))


def monitor(request):
    latest_light_value = Sensors.objects.order_by('-pub_date')[:2]
    template = loader.get_template('mqtt/index.html')
    context = {
        'latest_light_value': latest_light_value,
    }
    return HttpResponse(template.render(context, request))


def log(request):
    latest_light_value = Sensors.objects.order_by('-pub_date')
    template = loader.get_template('mqtt/index.html')
    context = {
        'latest_light_value': latest_light_value,
    }
    return HttpResponse(template.render(context, request))
