import django_filters
from .models import Attendance
from django_filters import rest_framework as filters


class AttendanceFilter(django_filters.FilterSet):
    class Meta:
        model = Attendance
        fields = ['staff']