__author__ = 'McDaemon'

from rest_framework import serializers

from pythonwetter.models import Weather
from pythonwetter.models import Feedback


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
        fields = ('id', 'kommentar', 'bewertung', 'user', 'mail', 'commentdatum', 'wetter', 'url')