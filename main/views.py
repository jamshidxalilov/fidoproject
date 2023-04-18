import calendar
from datetime import datetime, date, timezone

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.db.models import Sum
from django_filters.views import FilterView

from main.filter import AttendanceFilter
from main.models import Staff, Attendance, Months


class MainIndex(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        staffs = Staff.objects.order_by('?')
        context['staffs'] = staffs
        return context


class StaffAbout(DetailView):
    model = Staff
    template_name = 'pages/staff_about.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        month = datetime.now().month
        data = super().get_context_data()
        data['staff'] = Staff.objects.filter(id=self.object.pk)
        data['months'] = Months.objects.all()
        data['attendance'] = Attendance.objects.filter(staff_id=pk, enter_at__month=str(month)).order_by("-id")
        data['total_hours'] = [Attendance.objects.filter(staff_id=pk, enter_at__month=str(month)).aggregate(Sum('hours'))]
        # data['attendance_hours'] = Attendance.objects.filter(staff_id=pk, action_at__gte=date(2023, 5, 1))
        return data


def MonthFilter(request, pk):
    d = datetime(2023, pk, 1)
    print(d.month)
    staff = Staff.objects.filter(id=pk)
    total_hours = [Attendance.objects.filter(staff_id=pk).aggregate(Sum('hours'))]
    months = Months.objects.all()
    queryset = Attendance.objects.filter(enter_at__month=str(d.month))
    print(queryset)
    return render(request, "pages/staff_about.html", {
        "attendance": queryset,
        "months": months
    })

