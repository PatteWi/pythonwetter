import unittest
import coveralls
from django.test import Client


class TestServerAvailability(unittest.TestCase):
    def setUp(self):
        self.Client = Client()

    def testServer(self):
        response = self.Client.get('/weather/')
        self.assertEqual(response.status_code, 200)

    def testWeather(self):
        response = self.Client.get('/weathers/')
        self.assertEqual(response.status_code, 200)