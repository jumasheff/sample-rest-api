from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Fish
from .serializers import FishSerializer


class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer

