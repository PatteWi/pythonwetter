# -*- coding: UTF-8 -*-
__author__ = 'patrick'
from time import strftime

from pythonwetter.models import *
from pythonwetter.functions import *

WEATHER_URLY = 'http://xml.weather.yahoo.com/forecastrss?w=%s&u=c'
WEATHER_NSY = 'http://xml.weather.yahoo.com/ns/rss/1.0'

#cityarray = ['Potsdam', 'Berlin', 'Hamburg', 'Brandenburg, Havel', 'Aachen']
cityarray = list(City.objects.values_list('stadt', flat=True))

for city in cityarray:
    ########### Yahoo ###########
    woeid = stadtidy(city)
    url = WEATHER_URLY % woeid
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = []
    ycondition = dom.getElementsByTagNameNS(WEATHER_NSY, 'condition')[0]
    yastronomy = dom.getElementsByTagNameNS(WEATHER_NSY, 'astronomy')[0]
    ywind = dom.getElementsByTagNameNS(WEATHER_NSY, 'wind')[0]
    yunits = dom.getElementsByTagNameNS(WEATHER_NSY, 'units')[0]
    ywindspeed = str(ywind.getAttribute('speed'))
    ywindspeed = int(ywindspeed[:-3])
    winddir = windrichtung(int(ywind.getAttribute('direction')))
    unit = yunits.getAttribute('temperature')
    temperature = ycondition.getAttribute('temp')
    condition = str(ycondition.getAttribute('text'))
    code = int(ycondition.getAttribute('code'))
    title = dom.getElementsByTagName('title')[0].firstChild.data[16:]
    ######################
    ########### Wetter.com ###########
    citycode = stadtidw(city)
    dom = wwetter(citycode)
    wwindspeed = dom.getElementsByTagName('ws')[4].firstChild.data
    wwinddir = dom.getElementsByTagName('wd_txt')[4].firstChild.data
    wsunrise = 'keine Angabe'
    wsunset = 'keine Angabe'
    wtemp = 'keine Angabe'
    wcode = dom.getElementsByTagName('w')[4].firstChild.data
    wtitle = dom.getElementsByTagName('name')[0].firstChild.nodeValue + ", " + citycode[0:2]
    wcondition = dom.getElementsByTagName('w_txt')[4].firstChild.data
    wtemperature = dom.getElementsByTagName('tx')[4].firstChild.data
    yahoo = Weather(datum=strftime("%Y-%m-%d"), stadt=title, anbieter='Yahoo', wetter=condition,
                    tagestemperatur=temperature, einheit=unit, kondition=code, windgeschwindigkeit=ywindspeed,
                    windrichtung=winddir)
    if not Weather.objects.filter(datum=strftime("%Y-%m-%d"), stadt=title, anbieter='Yahoo').exists():
        print (yahoo)
        yahoo.save()
    else:
        print ("Datensatz ist bereits vorhanden")
    wettercom = Weather(datum=strftime("%Y-%m-%d"), stadt=wtitle, anbieter='Wetter.com', wetter=wcondition,
                        tagestemperatur=wtemperature, einheit=unit, kondition=wcode, windgeschwindigkeit=wwindspeed,
                        windrichtung=wwinddir)
    if not Weather.objects.filter(datum=strftime("%Y-%m-%d"), stadt=wtitle, anbieter='Wetter.com').exists():
        print (wettercom)
        wettercom.save()
    else:
        print ("Datensatz ist bereits vorhanden")

print ("Fertig")