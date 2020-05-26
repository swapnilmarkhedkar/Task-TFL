from rest_framework import serializers
from user_activity.models import Activity, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # @TODO: Change later

    class Meta:
        model = Activity
        fields = '__all__'
