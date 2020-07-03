
# Create your views here.
from django.http import Http404

from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from api.serializers import *


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ProduceViewSet(viewsets.ModelViewSet):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer
    parser_classes = [MultiPartParser]

    def list(self, request, *args, **kwargs):
        order = request.query_params.get('order')
        o_phone_num = request.query_params.get('o_phone_num')

        product = get_object_or_404(Produce, order=order, o_phone_num=o_phone_num)
        if product is None:
            raise Http404("No data")
        else:
            serializer = ProduceSerializer(product)
            return Response(serializer.data)
