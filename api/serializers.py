from rest_framework import serializers
from api.models import *


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class Test2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Test2
        fields = '__all__'
