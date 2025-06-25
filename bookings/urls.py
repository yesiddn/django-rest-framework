from django.urls import path
from .views import AppointmentListCreateView, MedicalNoteListCreateView, AppointmentDetailView, MedicalNoteDetailView

urlpatterns = [
    path(
        "appointments/", AppointmentListCreateView.as_view()
    ),  # Use as_view() to convert the class-based view into a callable view
    path(
        "appointments/<int:pk>/", AppointmentDetailView.as_view()
    ),  # Use AppointmentDetailView for detail views
    path(
        "medical-notes/", MedicalNoteListCreateView.as_view()
    ),  # Use as_view() to convert the class-based view into a callable view
    path(
        "medical-notes/<int:pk>/", MedicalNoteDetailView.as_view()
    ),  # Use MedicalNoteDetailView for detail views
]
