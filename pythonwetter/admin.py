from django.contrib import admin

from pythonwetter.models import *

admin.site.register(Weather)
admin.site.register(City)
admin.site.register(Feedback)