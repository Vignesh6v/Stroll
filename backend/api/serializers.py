from rest_framework import serializers
from models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('firstName','lastName','email','password')


class TourSerializezr(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = '__all__'
