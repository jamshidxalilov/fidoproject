from django.urls import path
from .views import MainIndex, StaffAbout, MonthFilter

app_name = "main"

urlpatterns = [
    path("", MainIndex.as_view(), name='index'),
    path("staff/<int:pk>/", StaffAbout.as_view(), name='staff'),
    path("month/<int:pk>/", MonthFilter, name='month'),
]