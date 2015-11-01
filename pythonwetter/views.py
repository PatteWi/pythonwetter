# -*- coding: iso-8859-15 -*-
import json

from django.shortcuts import render
from rest_framework import viewsets, filters
from pygeocoder import Geocoder
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext

from pythonwetter.getweather import *
from pythonwetter.serializers import *
from pythonwetter.functions import stadtidw
from pythonwetter.functions import stadtidy
from pythonwetter.models import *


def main(request):
   return render_to_response('weather_list.html', context_instance=RequestContext(request))

def ajax(request):
    if 'coords' in request.POST:
        x = request.POST['coords']
        y = x.split(",")
        try:
            z = Geocoder.reverse_geocode(float(y[0]), float(y[1]))
            z = z.city
            z = str(z)
        except:
            z = "konnte nicht lokalisiert werden"
        response_dict = {}
        response_dict.update({'server_response': z})
        return HttpResponse(json.dumps(response_dict), content_type='application/javascript')
    else:
        return render_to_response('weather_list.html', context_instance=RequestContext(request))

def get_weather_list(request):

    defaultcity = "Berlin"
    country = ", Germany"
    city = request.GET.get('city', '')
    if city == '':
        city = defaultcity

    ycity = city + ", Germany"
    warn = ""

    try:
        woe = stadtidy(ycity)
        wcity = ytowort(woe)
        citycode = stadtidw(wcity)
    except KeyError:
        city = defaultcity
        ycity = city + country
        woe = stadtidy(ycity)
        citycode = stadtidw(city)
        warn = u"Es wurden nicht unterstützte Umlaute gefunden. Bitte verwenden sie 'ae', 'oe' oder 'ue'!"
    except IndexError:
        city = defaultcity
        ycity = city + country
        woe = stadtidy(ycity)
        citycode = stadtidw(city)
        warn = u"Die gesuchte Stadt konnte leider nicht gefunden werden. Bitte wählen Sie eine andere Stadt!"

    orte = City.objects.order_by("stadt")

    weather_listy = yahoowetter(woe)
    weather_listw = wettercomwetter(citycode)
    return render(request, 'weather_list.html', {'page_title': 'Wetter in Python', 'yahoo_wetter': weather_listy,
                                                 'wetter_com': weather_listw, 'warning': warn, 'orte': orte },)

def get_index(request):
    return render(request, 'index.html')

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('datum', 'stadt')

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('wetter')