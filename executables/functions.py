import urllib, hashlib
from xml.dom import minidom

def wwetter(citycode):
    projektname = "pythonwetterfhb"
    apikey = "c5aa08dea1427f7a5a90762ccca6d430"
    apiurl = "http://api.wetter.com/forecast/weather/city/"
    checksum = hashlib.md5(projektname.encode('utf-8') + apikey.encode('utf-8') + citycode.encode('utf-8')).hexdigest()
    url = apiurl + citycode + "/project/" + projektname + "/cs/" + checksum
    dom = minidom.parse(urllib.request.urlopen(url))
    print(type(dom))
    return dom