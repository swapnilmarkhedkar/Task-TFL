from django.shortcuts import render
from django.http import HttpResponse, Http404
from user_activity.models import User, Activity
from user_activity.serializers import UserSerializer, ActivitySerializer, ActivityWithUserInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

import pprint
pp = pprint.PrettyPrinter(indent=4)


def index(request):
    return HttpResponse("Welcome to TFL Task by Swapnil Markhedkar. Refer to README.md for more info on API endpoints")


class UserList(generics.ListCreateAPIView):
    """
    @desc - List and create all users
    @route - GET|POST api/users/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    @desc - Retrieve, update or delete a user. Requires user id
    @route - GET|PATCH|DELETE api/users/<int:pk>/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityList(generics.ListCreateAPIView):
    """
    @desc - List and create activites
    @route - GET|POST api/acitivities/
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    @desc - Retrieve, update or delete an activity. Requires activity id
    @route - GET|PATCH|DELETE api/activities/<int:pk>/
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityWithUserInfoList(generics.ListAPIView):
    """
    @desc - List all activities along with user info
    @route - GET api/act-user/
    """
    queryset = Activity.objects.all()
    serializer_class = ActivityWithUserInfoSerializer


class ActivityWithUserInfoDetail(generics.ListAPIView):
    """
    @desc - List all activities of a particular user, along with user info. Requires user id
    @route - GET api/act-user/<int:pk>/
    """
    queryset = Activity.objects.all()
    serializer_class = ActivityWithUserInfoSerializer
