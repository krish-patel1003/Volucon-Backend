from django.urls import path
from .views import *
urlpatterns = [
    # path('create-profile/', OrgProfileView.as_view(), name='create-org-profile'),
    # path('update-profile/<int:user_id>', OrgProfileUpdate.as_view(), name='org-profile-update'),
    path('org-profile/', OrgProfileView.as_view(), name='org-profile'),
    path('org-detail/<int:user_id>', OrgDetailView.as_view(), name='org-detail'),
    path('event/', EventView.as_view(), name='create-event'),
    path('event/<int:event_id>', EventUpdateView.as_view(), name='event-update-delete'),
]