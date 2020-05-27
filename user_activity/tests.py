from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user_activity.serializers import ActivityWithUserInfoSerializer
from user_activity.models import User, Activity


class UserActivity(APITestCase):
    """
    Simple test case to check if the main task REST API end point fetches a 200
    """
    url = reverse('act_user')

    def test_activity_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
