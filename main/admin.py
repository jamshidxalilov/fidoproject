from django.contrib import admin
from django.forms import forms, ModelForm

from .models import Job, Department, Staff, Attendance


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        'fio',
        'job',
        'department',
        'hour_salary'
    ]


class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = [
            'staff',
            'enter_at',
            'leave_at',
            'hours']

    def clean(self):
        cleaned_data = super().clean()
        leave_at = cleaned_data.get("leave_at")
        enter_at = cleaned_data.get("enter_at")
        if enter_at > leave_at:
            raise forms.ValidationError("Kiritilgan sana noto'g'ri")
        return self.cleaned_data

    def _save_m2m(self, commit=True):

        if self.instance.leave_at:
            hour = self.instance.leave_at - self.instance.enter_at
            h = int(hour.total_seconds())
            print(self.instance.id)
            obj = Attendance.objects.filter(id=self.instance.id).update(hours=h)
        return obj


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    form = AttendanceForm
    list_display = [
        'staff',
        'enter_at',
        'leave_at',
        'hours'
    ]

    # def save_model(self, request, obj, form, change):
    #     if obj.leave_at:
    #         hour = obj.leave_at - obj.enter_at
    #         h = hour.total_seconds()
    #         Attendance.objects.filter(staff_id=obj.staff_id).update_or_create(hours=h)
    #     return super(AttendanceAdmin, self).save_model(request, obj, form, change)

