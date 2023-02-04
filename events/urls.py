from django.urls import path
from .views import show_vol_info

urlpatterns = [
    path('vol-info/', show_vol_info, name='vol-info'),
]