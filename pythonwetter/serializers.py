__author__ = 'McDaemon'

from models import Weather
from models import Feedback
from rest_framework import serializers


class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    feedback = serializers.Field

    class Meta:
        model = Weather
        depth = 1
        fields = ('id', 'feedback', 'datum', 'stadt', 'anbieter', 'wetter', 'tagestemperatur', 'einheit', 'kondition',
                 'windgeschwindigkeit', 'windrichtung', 'url')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'kommentar', 'bewertung', 'user', 'commentdatum', 'wetter', 'url')