# Generated by Django 4.1.6 on 2023-02-11 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='card', to=settings.AUTH_USER_MODEL),
        ),
    ]
