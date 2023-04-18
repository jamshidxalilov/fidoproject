from django.urls import path
from .views import MainIndex, StaffAbout, MonthFilter, LoadTable

app_name = "main"

urlpatterns = [
    path("", MainIndex.as_view(), name='index'),
    path("staff/<int:pk>/", StaffAbout.as_view(), name='staff'),
    path("month/<int:pk>/", MonthFilter, name='month'),
    path('load-table/<int:id>/', LoadTable.as_view(), name="load-table"),
]