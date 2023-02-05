from django_filters import rest_framework as filters
from .models import Event

class EventFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='from_date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='to_date', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['location', 'start_date', 'end_date']