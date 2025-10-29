from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['firstname', 'lastname', 'phonenumber', 'dob']

class UserRegisterSerializer(serializers.ModelSerializer):
    profile= UserProfileSerializer(required = False)

    class Meta:
        model = UserRegister
        fields = ['id', 'username', 'email', 'password', 'gender', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = UserRegister.objects.create(**validated_data)
        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)
        return user
        