from django.urls import path
from .views import DoctorView, DoctorDetailView

urlpatterns = [
    path("doctors/", DoctorView.as_view()), # Use as_view() to convert the class-based view into a callable view
    path("doctors/<int:pk>/", DoctorDetailView.as_view()),  # Use DoctorDetailView for detail views
]
