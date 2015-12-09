# -*- coding: utf-8 -*-
"""
Kardinalitaetsproblematik in Django
"""

from django.db import models


class Weather(models.Model):
    datum = models.DateField(max_length=32)
    stadt = models.CharField(max_length=32)
    anbieter = models.CharField(max_length=32)
    wetter = models.CharField(max_length=32)
    tagestemperatur = models.IntegerField(default=0)
    einheit = models.CharField(max_length=1)
    kondition = models.IntegerField(default=0)
    windgeschwindigkeit = models.IntegerField(default=1)
    windrichtung = models.CharField(max_length=2)

    def __str__(self):
        return str(self.datum) + ", " + self.stadt + ", " + self.anbieter

class Feedback(models.Model):
    kommentar = models.CharField(max_length=2000)
    bewertung = models.IntegerField(default=1)
    user = models.CharField(max_length=200)
    wetter = models.ForeignKey(Weather, related_name='feedback')
    commentdatum = models.DateTimeField(max_length=32)

    def __str__(self):
        return str(self.bewertung)

class City(models.Model):
    stadt = models.CharField(max_length=200)

    def __str__(self):
        return str(self.stadt)

