from django.core.validators import RegexValidator
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name="Город")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Speciality(models.Model):
    name = models.CharField(max_length=255, verbose_name="Специалисты")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"


class Patient(models.Model):
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
        return self.name

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"
