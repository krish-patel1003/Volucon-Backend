from profiles.models import VolunteerProfile
from users.models import User
from organizations.models import Organization, Event
from django.shortcuts import get_object_or_404
from profiles.serializers import VolunteerProfileSerializer

def get_vol_info(request):
    user = request.user
    print("user= ", user)
    v = VolunteerProfile.objects.get(user=1)
    data = VolunteerProfileSerializer(v).data
    print("volunteer_data=",v)
    return data