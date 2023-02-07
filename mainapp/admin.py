from django.contrib import admin

from mainapp.models import City, Speciality

admin.site.register([City, Speciality])