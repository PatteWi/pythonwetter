__author__ = 'Patrick'
import hashlib
import urllib
from xml.dom import minidom

import yweather


def windrichtung(winddir):
    if winddir <= 23:
        winddir = 'N'
    elif winddir <= 67:
        winddir = 'NE'
    elif winddir <= 113:
        winddir = 'E'
    elif winddir <= 158:
        winddir = 'SE'
    elif winddir <= 203:
        winddir = 'S'
    elif winddir <= 248:
        winddir = 'SW'
    elif winddir <= 293:
        winddir = 'W'
    elif winddir <= 338:
        winddir = 'NW'
    else:
        winddir = 'nn'
    return winddir

def stadtidw(city):
    projektname = "pythonwetterfhb"
    apikey = "c5aa08dea1427f7a5a90762ccca6d430"
    checksum = hashlib.md5(projektname.encode('utf-8') + apikey.encode('utf-8') + city.encode('utf-8')).hexdigest()
    urlstart = "http://api.wetter.com/location/name/search/"
    cityURL = urlstart + city + "/project/" + projektname + "/cs/" + checksum
    url = cityURL
    dom = minidom.parse(urllib.request.urlopen(url))
    citycode = dom.getElementsByTagName('city_code')[0].firstChild.data
    return citycode

# Scheint gar nicht genutzt zu werden - evtl. entfernen
# def stadtidwurl(city):
#     projektname = "pythonwetterfhb"
#     apikey = "c5aa08dea1427f7a5a90762ccca6d430"
#     checksum = hashlib.md5(projektname.encode('utf-8') + apikey.encode('utf-8') + city.encode('utf-8')).hexdigest()
#     urlstart = "http://api.wetter.com/location/name/search/"
#     cityURL = urlstart + city + "/project/" + projektname + "/cs/" + checksum
#     url = cityURL
#     dom = minidom.parse(urllib.request.urlopen(url))
#     citycode = dom.getElementsByTagName('city_code')[0].firstChild.data
#     print(url)
#     return url

def stadtidy(city):
    client = yweather.Client()
    woe = client.fetch_woeid(city)
    return woe