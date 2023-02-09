from django.contrib import admin

from mainapp.models import City, Speciality, Patient

admin.site.register([City, Speciality, Patient])