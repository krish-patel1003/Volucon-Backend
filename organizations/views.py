from django.shortcuts import render
from rest_framework.response import Response
from .serializers import OrgProfileSerializer, EventSerializer
from .models import Organization, Event
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .permissions import IsUserItself, IsOwnerOrg
from users.models import User
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

# Create your views here.

class OrgProfileView(APIView):
    serializer_class = OrgProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = Organization.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response({"data":serializer.data, "msg":"all orgs"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"data": serializer.data, "msg": "Org Profile created"}, status=status.HTTP_201_CREATED)

        return Response(
            {"error": serializer.errors, "msg": "Org Profile not created"}, status=status.HTTP_400_BAD_REQUEST)


class OrgDetailView(APIView):
    serializer_class = OrgProfileSerializer
    permission_classes = [IsAuthenticated, IsUserItself]

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        profile = Organization.objects.get(user=user)
        serializer = OrgProfileSerializer(profile)
        return Response({"data": serializer.data, "msg": "Profile fetched"}, status=status.HTTP_200_OK)

    def patch(self, request, user_id):
        user = User.objects.get(id=user_id)
        profile = Organization.objects.get(user=user)

        serializer = OrgProfileSerializer(
            profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "msg": "Profile Updated"}, status=status.HTTP_200_OK)

        return Response({"error": serializer.errors, "msg": "Invalid Data input"}, status=status.HTTP_400_BAD_REQUEST)


class EventView(APIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = Event.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response({"data":serializer.data, "msg":"all events"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"data": serializer.data, "msg": "Event created"}, status=status.HTTP_201_CREATED)

        return Response(
            {"error": serializer.errors, "msg": "Event not created"}, status=status.HTTP_400_BAD_REQUEST)

class EventUpdateView(APIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrg]

    def get(self, request, event_id):
        event = Event.objects.get(id=event_id)
        serializer = self.serializer_class(event)
        return Response({"data":serializer.data, "msg":"Event"}, status=status.HTTP_200_OK)

    def patch(self, request, event_id):
        org = Organization.objects.get(user=request.user)
        event = Event.objects.get(id=event_id, organization=org)
        serializer = EventSerializer(
            event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "msg": "Event Updated"}, status=status.HTTP_200_OK)

        return Response({"error": serializer.errors, "msg": "Invalid Data input"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id):
        event = Event.objects.get(id=event_id)
        event.delete()
        return Response({"msg":"event successfully deleted"}, status=status.HTTP_200_OK)
