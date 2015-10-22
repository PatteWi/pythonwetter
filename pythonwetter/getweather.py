# -*- coding: utf-8 -*-
__author__ = 'patrick'

import urllib
import hashlib
from xml.dom import minidom

from functions import windrichtung



########## Wetter von Yahoo ##########
WEATHER_URLY = 'http://xml.weather.yahoo.com/forecastrss?w=%s&u=c'
WEATHER_NSY = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def yahoowetter(woeid):
    url = WEATHER_URLY % woeid
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = []
    for node in dom.getElementsByTagNameNS(WEATHER_NSY, 'forecast'):
        forecasts.append({
            'date': node.getAttribute('date'),
            'low': node.getAttribute('low'),
            'high': node.getAttribute('high'),
            'condition': node.getAttribute('text'),
            'code': node.getAttribute('code'),
            'windspeed': 'n.v.',
            'winddirection': 'n.v.',
            })
    ycondition = dom.getElementsByTagNameNS(WEATHER_NSY, 'condition')[0]
    yastronomy = dom.getElementsByTagNameNS(WEATHER_NSY, 'astronomy')[0]
    ywind = dom.getElementsByTagNameNS(WEATHER_NSY, 'wind')[0]
    yunits = dom.getElementsByTagNameNS(WEATHER_NSY, 'units')[0]
    return {
        'windspeed': ywind.getAttribute('speed'),
        'winddirection': windrichtung(int(ywind.getAttribute('direction'))),
        'utemp': yunits.getAttribute('temperature'),
        'sunrise': yastronomy.getAttribute('sunrise'),
        'temp': ycondition.getAttribute('temp'),
        'sunset': yastronomy.getAttribute('sunset'),
        'current_condition': ycondition.getAttribute('text'),
        'current_temp': ycondition.getAttribute('temp'),
        'code': ycondition.getAttribute('code'),
        'forecasts': forecasts,
        'title': dom.getElementsByTagName('title')[0].firstChild.data
    }

def ytowort(woeid):
    url = WEATHER_URLY % woeid
    dom = minidom.parse(urllib.urlopen(url))
    yort = dom.getElementsByTagNameNS(WEATHER_NSY, 'location')[0]
    ort = yort.getAttribute('city')
    return ort

def wettercomwetter(stadtcode):
    apiurl = "http://api.wetter.com/forecast/weather/city/"
    citycode = stadtcode

    projektname = "pythonwetterfhb"
    apikey = "c5aa08dea1427f7a5a90762ccca6d430"
    checksum = hashlib.md5(projektname + apikey + citycode).hexdigest()
    url = apiurl + citycode + "/project/" + projektname + "/cs/" + checksum
    dom = minidom.parse(urllib.urlopen(url))
    forecastsw = []
    for node in dom.getElementsByTagName('date'):
        forecastsw.append({
            'windspeed': node.getElementsByTagName('ws')[4].firstChild.data,
            'winddirection': node.getElementsByTagName('wd_txt')[4].firstChild.data,
            'date': node.getAttribute('value'),
            'low': node.getElementsByTagName('tn')[4].firstChild.data,
            'high': node.getElementsByTagName('tx')[4].firstChild.data,
            'condition': node.getElementsByTagName('w_txt')[4].firstChild.data,
            'code': node.getElementsByTagName('w')[4].firstChild.data
        })
    return {
        'windspeed': dom.getElementsByTagName('ws')[4].firstChild.data,
        'winddirection': dom.getElementsByTagName('wd_txt')[4].firstChild.data,
        'sunrise': 'keine Angabe',
        'sunset': 'keine Angabe',
        'forecastsw': forecastsw,
        'temp': 'keine Angabe',
        'code': dom.getElementsByTagName('w')[4].firstChild.data,
        'title': dom.getElementsByTagName('name')[0].firstChild.nodeValue + ", " + stadtcode[0:2],
        'condition': dom.getElementsByTagName('w_txt')[4].firstChild.data
    }

