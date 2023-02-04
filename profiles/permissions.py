from rest_framework.permissions import BasePermission
from .models import VolunteerProfile
from users.models import User


class IsUserItself(BasePermission):

    def has_object_permission(self, request, view, obj):
        profile = VolunteerProfile.objects.get(user=request.user)
        return profile == obj