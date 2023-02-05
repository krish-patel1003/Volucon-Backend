from django.urls import path
from .views import *
urlpatterns = [
    path('recommended/', RecommendedEvents.as_view(), name="volinfo"),
]