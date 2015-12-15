import unittest

from urllib.request import urlopen
from django.test import Client, TestCase
from pythonwetter.functions import stadtidy, windrichtung, stadtidw


class TestServerAvailability(unittest.TestCase):
    def setUp(self):
        self.Client = Client()

    def testServer(self):
        response = self.Client.get('/weather/')
        self.assertEqual(response.status_code, 200)

    def testWeather(self):
        response = self.Client.get('/weathers/')
        self.assertEqual(response.status_code, 200)

    def testWetterBrandenburg(self):
        response = self.Client.get('/weather/?city=Brandenburg+an+der+Havel')
        self.assertEqual(response.status_code, 200)

    def testWetterUngueltig(self):
        response = self.Client.get('/weather/?city=fdjkvöoevlnvioüribfnreiogblmflbgkln§%24%25%26%2F%28%29%3D%29%28%2F%26%25%24§%24%25%26%2F%28%29%3D%29%28%2F%26%25%24§%24%25%26%2F%28%29%3D&')
        self.assertEqual(response.status_code, 200)

    def testWeathersearch(self):
        response = self.Client.get('/weathersearch?datum=2015-12-15&stadt=Berlin')
        self.assertEqual(response.status_code, 200)

    def testSendMailFail(self):
         response = self.Client.get('/send_mail')
         self.assertEqual(response.status_code, 200)

    def testSendMailSuccess(self):
         response = self.Client.get('/send_mail?name=Travis&kommentar=Der Test war erfolgreich')
         self.assertEqual(response.status_code, 200)

class TestS3(TestCase):
    def testS3Available(self):
        response = urlopen('https://s3.amazonaws.com/pythonwetter/static/images/wc/d_0_L.png')
        self.assertEqual(response.getcode(), 200)


class TestFunktions(unittest.TestCase):

    def testYahooStadtID(self):
        woe = stadtidy('Potsdam')
        self.assertEqual(woe, '685783')

    def testWindrichtungen(self):
        winddirs = [20, 60, 110, 150, 160, 210, 260, 310, 500]
        results = []
        for winddir in winddirs:
            result = windrichtung(winddir)
            results.append(result)
        self.assertListEqual(results, ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'nn'])

    def testCitycode(self):
        stadt = 'Potsdam'
        self.assertEqual(stadtidw(stadt), 'DE0008362')
