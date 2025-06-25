from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializer, MedicalNoteSerializer

# los genericos son clases que proporcionan implementaciones comunes de las vistas de la API RESTful, como ListCreateAPIView y RetrieveUpdateDestroyAPIView.
# ListCreateAPIView maneja las operaciones de lista y creación, mientras que RetrieveUpdateDestroyAPIView maneja la recuperación, actualización y eliminación de un objeto específico.
# Estas clases permiten crear vistas de API RESTful de manera más sencilla y rápida, ya que manejan automáticamente las operaciones comunes de la API.
# en este link se encuentra la documentacion https://www.cdrf.co/
class AppointmentListCreateView(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalNoteListCreateView(ListCreateAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer

class AppointmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class MedicalNoteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer
    