# Generated by Django 4.1.6 on 2023-02-06 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "working_place",
                    models.CharField(max_length=255, verbose_name="Место работы"),
                ),
                (
                    "propic",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="propics/",
                        verbose_name="Фотография",
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="doctors",
                        to="mainapp.city",
                    ),
                ),
                (
                    "speciality",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="doctors",
                        to="mainapp.speciality",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Доктор",
                "verbose_name_plural": "Доктора",
            },
        ),
    ]
