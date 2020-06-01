from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class Test2ViewSet(viewsets.ModelViewSet):
    queryset = Test2.objects.all()
    serializer_class = Test2Serializer
