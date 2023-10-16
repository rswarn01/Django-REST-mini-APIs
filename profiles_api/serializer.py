from rest_framework import serializers
from .models import UserProfile, ProfileFeedItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["name", "email", "is_superuser", "is_staff"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["name", "email", "is_superuser", "is_staff"]
        extra_kwrgs = {
            "password": {"write_only": True},
            "style": {"input_type": "password"},
        }


class ProfileFeedSerializer(serializers.ModelSerializer):
    """serializer profile feed items"""

    class Meta:
        model = ProfileFeedItem
        fields = ("id", "user_profile", "status_text", "created_on")
        extra_kwargs = {"user_profile": {"read_only": True}}
