from django.db import models

from django.core.validators import RegexValidator

from doctors.models import Doctor


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='Лечащий врач', on_delete=models.CASCADE, related_name='appointment')
    name = models.CharField(max_length=255, verbose_name='Ваше имя')
    phone_number = models.CharField(
        validators=[RegexValidator(
            regex='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',
            message='phone number must be digits',
            code='invalid phone number'
        )],
        max_length=15
    )
    email = models.EmailField(
        verbose_name="Ваша почта",
        max_length=255,
        unique=True,
    )
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}: {self.email}, {self.phone_number}'

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"
