from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from GolfStatsApp import models
from .serializers import GolfStatsAppSerializer

class ListUser(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = GolfStatsAppSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = GolfStatsAppSerializer