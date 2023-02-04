from rest_framework.permissions import BasePermission
from .models import Organization
from users.models import User


class IsUserItself(BasePermission):

    def has_object_permission(self, request, view, obj):
        profile = Organization.objects.get(user=request.user)
        return profile == obj

class IsOwnerOrg(BasePermission):

    def has_object_permission(self, request, view, obj):
        org = Organization.objects.get(user=request.user)
        return obj.organization == org