from rest_framework import serializers
from .models import Organization, Event

class OrgProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'
    

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'