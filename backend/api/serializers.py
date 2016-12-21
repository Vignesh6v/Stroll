from rest_framework import serializers
from django.forms import ModelForm
from models import *

class PhotoForm(serializers.ModelSerializer):
    class Meta:
        model = Upload
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
