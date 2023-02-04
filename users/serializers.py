from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.conf import settings
from .utils import get_tokens_for_user

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=validated_data['password'])

        return user