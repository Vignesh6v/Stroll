from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import services as appservice
from . import mapping
from serializers import UserSerializer

# User Sign Up
@api_view(['POST'])
def userSignup(request):
    userexist = appservice.searchuser(request.data['email'])
    if userexist:
         return Response('Already Registered',status=status.HTTP_409_CONFLICT)
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            result = appservice.insertuser(serializer.data)
            return Response('Signed Up', status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login
@api_view(['POST'])
def userLogin(request):
    # need to modify - have to check with password and email
    userexist = appservice.searchuser(request.data['email'])
    if userexist:
         return Response('Logged In',status=status.HTTP_200_OK)
    else:
        return Response('Need to Sign Up', status=status.HTTP_401_UNAUTHORIZED)

# List all available users
@api_view(['GET'])
def userList(request):
    if request.method != 'GET':
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        result = appservice.listofusers()
        serializer = UserSerializer(result, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def tourlist(request):
    # need to start
    pass
