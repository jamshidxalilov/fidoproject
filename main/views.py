from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from main.models import Staff, Attendance


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
        data = super().get_context_data()
        data['staff'] = Staff.objects.filter(id=self.object.pk)
        data['attendance'] = Attendance.objects.filter(staff_id=pk)
        print(data)
        return data