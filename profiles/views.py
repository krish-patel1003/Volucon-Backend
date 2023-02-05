from django.shortcuts import render
from .models import VolunteerProfile
from .serializers import VolunteerProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsUserItself
from users.models import User
# Create your views here.


class VolunteerProfileView(APIView):
    serializer_class = VolunteerProfileSerializer
    queryset= VolunteerProfile.objects.all()
    permission_classes = [IsAuthenticated]

    # @permission_classes((IsAdminUser,))
    def get(self, request, format=None):
        data = VolunteerProfile.objects.all()
        serializer = self.serializer_class(data, many=True)
        return Response({"data":serializer.data, "msg":"all volunteers"}, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"data": serializer.data, "msg": "Volunteer Profile created"}, status=status.HTTP_201_CREATED)

        return Response(
            {"error": serializer.errors, "msg": "Volunteer Profile not created"}, status=status.HTTP_400_BAD_REQUEST)


class VolunteerProfileDetail(APIView):
    serializer_class = VolunteerProfileSerializer
    permission_classes = [IsAuthenticated, IsUserItself]

    def get(self, request, user_id):
        profile = VolunteerProfile.objects.get(user=request.user)
        serializer = self.serializer_class(profile)
        return Response({"data": serializer.data, "msg": "Volunteer"}, status=status.HTTP_200_OK)


    def patch(self, request, user_id):
        profile = VolunteerProfile.objects.get(user=request.user)

        serializer = VolunteerProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "msg":"Profile Updated"}, status=status.HTTP_200_OK)

        return Response({"error": serializer.errors, "msg":"Invalid Data input"}, status=status.HTTP_400_BAD_REQUEST)
