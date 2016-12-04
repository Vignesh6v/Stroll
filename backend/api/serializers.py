from rest_framework import serializers
from models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('firstName','lastName','email','password')


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stops
        fields = '__all__'
