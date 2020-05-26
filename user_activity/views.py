from django.shortcuts import render
from django.http import HttpResponse
from user_activity.models import User, Activity

# Create your views here.
def index(request):
    # print(User.objects.filter())
    print(Activity.objects.filter(user_id=1).values())
    return HttpResponse("Hello, world")