from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import services as appservice
from . import mapping
from serializers import UserSerializer, TourSerializer, StopSerializer

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
    try:
        if not appservice.searchuser(request.data['email']):
            return Response('Need to Sign Up', status=status.HTTP_401_UNAUTHORIZED)
        authuser = appservice.logincheck(request.data['email'],request.data['password'])
        if authuser:
             return Response('Logged In',status=status.HTTP_200_OK)
        else:
            return Response('Password Error', status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)

# List all available users
@api_view(['GET'])
def userList(request):
    result = appservice.listofusers()
    serializer = UserSerializer(result, many=True)
    return Response(serializer.data)


# List of all Tours
@api_view(['GET'])
def tourlist(request):
    result = appservice.listofTours()
    serializer = TourSerializer(result, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


# Specific Tour details
@api_view(['GET','POST'])
def tourdetail(request, tour_id):
    if request.method == 'GET':
        result = appservice.specificTour(tour_id)
        return Response(tour_id,status=status.HTTP_200_OK)

    # To enter a Tour taken by the user
    # entering a record in history table
    elif request.method == 'POST':
        try:
            userid = request.data['email']
            if not appservice.tourTaken(tour_id,userid):
                return Response('Tour Taken', status=status.HTTP_201_CREATED)
            else:
                return Response('Tour Taken', status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def historydetail(request, user_id):
    result = appservice.userhistory(user_id)
    return Response(user_id)


@api_view(['GET'])
def historylist(request):
    result = appservice.fullhistory()
    return Response(result)

@api_view(['POST'])
def upload(request,stop_id):
    pass

@api_view(['POST'])
def createTour(request):
    try:
        t = request.data['tour']
        stops = request.data['stops']
        locationlist = []
        for x in stops:
            locationlist.append(dict(latitude=x['stop_latitude'] ,longitude=x['stop_longitude']))
        extradetails = appservice.finddistance(locationlist)
        tour = t.copy()
        tour.update(extradetails)
        tourserializer = TourSerializer(data=tour)
        if not tourserializer.is_valid():
            return Response(tourserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        stopserializer = StopSerializer(data=stops, many=True)
        if not stopserializer.is_valid():
            return Response(stopserializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if not appservice.createtour(tour,stops):
            return Response('Not Created', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Tour Created', status=status.HTTP_201_CREATED)
    except Exception as e:
        print 'got here'
        return Response(e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
