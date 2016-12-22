from rest_framework import serializers
from django import forms
from models import *

class PhotoForm(serializers.ModelSerializer):

    photo = serializers.ImageField(max_length=None, use_url= True)

    class Meta:
        model = Pictures
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class StopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stops
        fields = '__all__'
