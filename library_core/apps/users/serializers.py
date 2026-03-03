from rest_framework import serializers
from .models import MemberProfile, User
from rest_framework import serializers
from django.db import transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MemberProfileSerializer(serializers.ModelSerializer):
    # READ: nested user
    user = UserSerializer(read_only=True)

    # WRITE: user fields
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True, required=False)
    phone_number = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = MemberProfile
        fields = [
            "id",
            "membership_id",
            "id_proof_type",
            "id_proof_number",

            # read
            "user",

            # write
            "username",
            "password",
            "email",
            "phone_number",
        ]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        username = validated_data.pop("username")
        password = validated_data.pop("password")
        email = validated_data.pop("email", "")
        phone_number = validated_data.pop("phone_number", "")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )

        user.phone_number = phone_number
        user.save()

        member = MemberProfile.objects.create(
            user=user,
            **validated_data
        )

        return member

