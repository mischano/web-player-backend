from django.urls import path
from .views import search_audio_url

urlpatterns = [
    path('search-audio-url/', search_audio_url, name='search_audio_url'),
]
