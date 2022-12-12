from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
import requests
from rest_framework.response import Response
from django.contrib.postgres.search import SearchQuery

from rest_framework import viewsets

from .serializers import SongSerializer
from .models import Song

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import urllib
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def searchTitle(request, term, color=''):
    songs = ''
    decoded_term = urllib.parse.unquote(term)
    if decoded_term == '---noval---':
        songs = Song.objects.filter(color__iexact=color)
    elif color:
        songs = Song.objects.filter(title__search=decoded_term).filter(color__iexact=color)
    else:
        songs = Song.objects.filter(title__search=decoded_term)
    return Response(SongSerializer(songs, many=True).data)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def searchLyrics(request, term, color=''):
    songs = ''
    decoded_term = urllib.parse.unquote(term)
    if decoded_term == '---noval---':
        songs = Song.objects.filter(color__iexact=color)
    elif color:
        songs = Song.objects.filter(lyrics__search=decoded_term).filter(color__iexact=color)
    else:
        songs = Song.objects.filter(lyrics__search=decoded_term)
    return Response(SongSerializer(songs, many=True).data)