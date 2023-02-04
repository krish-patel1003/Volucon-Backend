from django.shortcuts import render
from .utils import get_vol_info
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def show_vol_info(request):
    data = get_vol_info(request)

    return Response({"data":data}, status=status.HTTP_200_OK)