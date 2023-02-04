from django.urls import path
from .views import *

urlpatterns = [
    path('volunteer-profile/', VolunteerProfileView.as_view(), name='create-vol-profile'),
    path('detail/<int:user_id>', VolunteerProfileDetail.as_view(), name='update-profile'),
]