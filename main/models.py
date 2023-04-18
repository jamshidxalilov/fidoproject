from datetime import datetime

from django.db import models

from fido.helpers import UploadTo


class Department(models.Model):
    """Aniq, Tabiiy, Ijtimoiy fanlar"""
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = ('Bo\'lim')
        verbose_name_plural = ('Bo\'limlar')

    def __str__(self):
        return self.name


class Job(models.Model):
    """Ona tili va adabiyoti, Matematika"""
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = ('Ish turi')
        verbose_name_plural = ('Ish turlari')

    def __str__(self):
        return self.name


class Staff(models.Model):
    """Ishchi"""
    photo = models.ImageField(UploadTo, upload_to='staffs', blank=True, null=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    job = models.ForeignKey(Job, on_delete=models.RESTRICT)
    department = models.ForeignKey(Department, on_delete=models.RESTRICT)
    hour_salary = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        verbose_name = ('Xodim')
        verbose_name_plural = ('Xodimlar')

    @property
    def fio(self):
        return "{} {}".format(self.last_name, self.first_name).strip()

    def __str__(self):
        return self.fio


class Attendance(models.Model):
    """Davomat"""

    # ACTION_IN = 1
    # ACTION_OUT = 0
    #
    # ACTIONS = (
    #     (ACTION_IN, 'Enter'),
    #     (ACTION_OUT, 'Leave')
    # )

    staff = models.ForeignKey(Staff, on_delete=models.RESTRICT)
    enter_at = models.DateTimeField()
    leave_at = models.DateTimeField(blank=True, null=True)
    hours = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return str(self.staff)

    class Meta:
        verbose_name = ('Ish davomati')
        verbose_name_plural = ('Ish davomati')


class Months(models.Model):
    MONTH = (
        (1, ("Yanvar")),
        (2, ("Fevral")),
        (3, ("Mart")),
        (4, ("Aprel")),
        (5, ("May")),
        (6, ("Iyun")),
        (7, ("Iyul")),
        (8, ("Avgust")),
        (9, ("Sentyabr")),
        (10, ("Oktyabr")),
        (11, ("Noyabr")),
        (12, ("Dekabr")),
    )

    month = models.SmallIntegerField(default=100, choices=MONTH)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name