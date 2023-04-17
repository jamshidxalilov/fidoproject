from django.urls import path
from .views import MainIndex, StaffAbout

app_name = "main"

urlpatterns = [
    path("", MainIndex.as_view(), name='index'),
    path("staff/<int:pk>/", StaffAbout.as_view(), name='staff'),
]