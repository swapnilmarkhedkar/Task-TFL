from django.shortcuts import render
from django.http import HttpResponse, Http404
from user_activity.models import User, Activity
from user_activity.serializers import ActivitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request):
    # print(User.objects.filter())
    print(Activity.objects.filter(user_id=1).values())
    return HttpResponse("Hello, world")


class ActivityList(APIView):
    """
    Lists all activites
    """

    def get(self, request, format=None):
        activities = Activity.objects.filter(user_id=1)
        serializer = ActivitySerializer(activities, many=True)
        print(serializer.data)
        return Response(serializer.data)
