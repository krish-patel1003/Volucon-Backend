from django.urls import path
from .views import VolunteerProfileView, ListVolunteers, VolunteerProfileUpdate

urlpatterns = [
    path('create/', VolunteerProfileView.as_view(), name='create-vol-profile'),
    path('update/<int:user_id>', VolunteerProfileUpdate.as_view(), name='update-profile'),
    path('', ListVolunteers.as_view(), name='profiles'),
]