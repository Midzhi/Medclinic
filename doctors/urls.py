from django.urls import path

from doctors.views import (
    DoctorListAPIView,
    DoctorDetailAPIView
)


urlpatterns = [
    path('doctors/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor-detail'),
    path('doctors/', DoctorListAPIView.as_view(), name='doctor-list')
]
