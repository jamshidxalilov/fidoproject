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

    ACTION_IN = 1
    ACTION_OUT = 0

    ACTIONS = (
        (ACTION_IN, 'Enter'),
        (ACTION_OUT, 'Leave')
    )

    staff = models.ForeignKey(Staff, on_delete=models.RESTRICT)
    action = models.SmallIntegerField(choices=ACTIONS)
    action_at = models.DateTimeField()

    def __str__(self):
        return str(self.action)

    class Meta:
        verbose_name = ('Ish davomati')
        verbose_name_plural = ('Ish davomati')