# -*- coding: iso-8859-15 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from views import WeatherViewSet
from views import CommentViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'weathers', WeatherViewSet)
router.register(r'comments', CommentViewSet)



urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^weather/$', 'pythonwetter.views.get_weather_list', name='PythonWeather'),
                       url(r'^index/$', 'pythonwetter.views.get_index', name='PythonWeather'),
                       url(r'^accounts/', include('allauth.urls')),
                       url(r'^weathersearch$', 'pythonwetter.views.get_index', name='PythonWeather'),
                       url(r'^weathers?(?P<pk>[0-9]+)/$', WeatherViewSet.as_view(),name='searchlist'),
                       url(r'^comments?(?P<pk>[0-9]+)/$', CommentViewSet.as_view(),name='searchcommentlist'),
                       url(r'^weather_json$', 'pythonwetter.views.ajax'),
                       )