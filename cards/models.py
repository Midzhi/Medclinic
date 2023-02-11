from django.db import models

from doctors.models import Doctor

from users.models import User


class Card(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="card")
    schedule = models.CharField(max_length=255, verbose_name='График работы')
    workload = models.CharField(max_length=255, verbose_name='Загруженность по приемам')
    price = models.IntegerField(verbose_name='Стоимость приема')

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
