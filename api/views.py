from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ProduceViewSet(viewsets.ModelViewSet):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer
