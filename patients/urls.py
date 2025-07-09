from django.urls import path
from .views import patient, patient_detail

urlpatterns = [
  path("", patient),
  path("<int:pk>/", patient_detail),
]
