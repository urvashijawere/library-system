from rest_framework import serializers
from .models import MemberProfile, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class MemberProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberProfile
        fields = "__all__"

