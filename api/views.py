from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from GolfStatsApp import models
from .serializers import GolfStatsAppSerializer

class ListRound(generics.ListCreateAPIView):
    queryset = models.Round.objects.all()
    serializer_class = GolfStatsAppSerializer

class DetailRound(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Round.objects.all()
    serializer_class = GolfStatsAppSerializer