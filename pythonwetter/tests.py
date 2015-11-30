import unittest, doctest

from django.test import Client
from pythonwetter.functions import stadtidy


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


class TestFunktions(unittest.TestCase):

    def testYahooStadtID(self):
        woe = stadtidy('Potsdam')
        self.assertEqual(woe, '685783')
