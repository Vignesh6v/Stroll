from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser

import services as appservice
from . import mapping
from serializers import UserSerializer, TourSerializer, StopSerializer, PhotoForm

# User Sign Up
@api_view(['POST'])
def userSignup(request):
    try:
        userexist = appservice.searchuser(request.data['email'])
        if userexist:
             return Response({'status': False ,'data':None, 'message':"Already Signed-up"},status=status.HTTP_409_CONFLICT)
        else:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                result = appservice.insertuser(serializer.data)
                #print result
                return Response({'status': True ,'data':result['_id'], 'message':None}, status=status.HTTP_201_CREATED)
            else:
                return Response({'status': False ,'data':None, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'status': False ,'data':None, 'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)

# User Login
@api_view(['POST'])
def userLogin(request):
    # need to modify - have to check with password and email
    try:
        if not appservice.searchuser(request.data['email']):
            return Response({'status': False ,'data':None, 'message':"Need to Sign-up"}, status=status.HTTP_401_UNAUTHORIZED)
        authuser = appservice.logincheck(request.data['email'],request.data['password'])
        print authuser
        if authuser:
             return Response({'status': True ,'data':authuser, 'message': None},status=status.HTTP_200_OK)
        else:
            return Response({'status': False ,'data':None, 'message':"password error"}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'status': False,'data': None, 'message': str(e)} , status=status.HTTP_400_BAD_REQUEST)

# List all available users
@api_view(['GET'])
def userList(request):
    try:
        result = appservice.listofusers()
        serializer = UserSerializer(result, many=True)
        return Response ({'status': True ,'data':serializer.data, 'message':''})
    except Exception as e:
        return Response({'status': False ,'data':None, 'message':str(e)} , status=status.HTTP_400_BAD_REQUEST)

# Update user profile
@api_view(['POST'])
def userEdit(request):
    try:
        print request.data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            #print "valid"
            #print serializer.data
            return Response({'status': True ,'data':None, 'message':'Updated'},status=status.HTTP_200_OK)
        else:
            return Response({'status': False ,'data':None, 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'status': False ,'data':None, 'message':str(e)} , status=status.HTTP_400_BAD_REQUEST)




# List of all Tours
@api_view(['GET'])
def tourlist(request):
    try:
        result = appservice.listofTours()
        serializer = TourSerializer(result, many=True)
        return Response({'status': True ,'data':serializer.data, 'message':None} ,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'status': False ,'data':None, 'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Specific Tour details
@api_view(['GET','POST'])
def tourdetail(request, tour_id):
    if request.method == 'GET':
        try:
            result = appservice.specificTour(tour_id)
            return Response({'status': True ,'data':result, 'message':None} ,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': False ,'data':None, 'message':str(e)} ,status=status.HTTP_400_BAD_REQUEST)


    # To enter a Tour taken by the user
    # entering a record in history table
    elif request.method == 'POST':
        try:
            userid = request.data['userid']
            if appservice.tourTaken(tour_id,userid):
                return Response({'status': True ,'data':None, 'message':'Tour taken'} , status=status.HTTP_201_CREATED)
            else:
                return Response({'status': False ,'data':None, 'message':'Tour Not taken'} , status=status.HTTP_409_CONFLICT)
        except Exception as e:
            return Response({'status': False ,'data':None, 'message':str(e)} ,status=status.HTTP_400_BAD_REQUEST)


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
            return Response({'status': False ,'data':None, 'message':'Not Created'} , status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': True ,'data':None, 'message':'Created'} , status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'status': False ,'data':None, 'message':str(e)} ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def enterComment(request,stop_id):
    try:
        result = appservice.entercomment(stop_id,request.data)
        return Response({'status': True ,'data':None, 'message':'Comment Entered'} , status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'status': False ,'data':None, 'message':str(e)} ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def stopDetails(request,stop_id):
    try:
        comments = appservice.stopdeatils(stop_id)
        photo_urls = appservice.getPhotos(stop_id)
        photo_urls = ['https://s3-us-west-2.amazonaws.com/cloud-stroll-images/Media/Quotefancy-24796-3840x2160.jpg', 'https://s3-us-west-2.amazonaws.com/cloud-stroll-images/Media/web-street.jpeg']
        stopname = appservice.getStopName(stop_id)
        result = {'comments': comments, 'photo_urls': photo_urls, 'Name':stopname }
        return Response({'status': True ,'data':result, 'message':None} ,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'status': False ,'data':None, 'message':str(e)} ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def historydetail(request, user_id):
    try:
        result = appservice.userhistory(user_id)
        return Response({'status': True ,'data':result, 'message':None})
    except Exception as e:
        return Response({'status': False ,'data':None, 'message':str(e)},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def historylist(request):
    try:
        result = appservice.fullhistory()
        return Response({'status': True ,'data':result, 'message':None} )
    except Exception as e:
        return Response({'status': False ,'data':None, 'message':str(e)} ,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def upload(request,stop_id,format=None):
    print request.POST
    print request.FILES
    print stop_id
    form = PhotoForm(request.POST, request.FILES)
    #print form
    if form.is_valid():
        print "good"
        print form
    else:
        return Response({'status': False ,'data':None, 'message':'Not Allowed'},status=status.HTTP_400_BAD_REQUEST)
