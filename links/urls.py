from django.urls import path
from .views import calculate, calculate_events

urlpatterns = [
    path('', calculate, name='links'),
    path('events', calculate_events, name = 'links_events')
]
    