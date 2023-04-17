from django.contrib import admin
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


@admin.register(Attendance)
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        'staff',
        'action',
        'action_at'
    ]


