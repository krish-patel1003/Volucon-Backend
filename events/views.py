from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .utils import get_info
from organizations.models import Event
from organizations.serializers import EventSerializer
# Create your views here.

@api_view(['GET'])
def vol_info(request):
    print(request._request)
    data = get_info(request)
    if data:
        return Response({"Data":"Success"})
    return Response({"Failure":"fail"})

class RecommendedEvents(APIView):
    serializer_class = EventSerializer

    def get(self, request, format=None):
        events = Event.objects.all()
        print("self.request=", self.request)
        print("request=", request)
        data = get_info(request)
        if data:
            recommended = []
            preferences = data.get('preferences')
            for p in preferences:
                for e in events:
                    r = e.requirement
                    if r:
                        for ri in r:
                            if p == ri:
                                recommended.append(e)
                                break
            serializer = self.serializer_class(recommended, many=True)
            return Response({"data":serializer.data, "msg":"recommended opportunities"})
            

        return Response({"Bad Request":"No Data"})  


    


