from django.urls import path
from .views import patient, patient_detail

urlpatterns = [
  path("patients/", patient),
  path("patients/<int:pk>/", patient_detail),
]
