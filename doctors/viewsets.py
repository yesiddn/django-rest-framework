from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Doctor, Department, MedicalNote, DoctorAvailability
from .serializers import DoctorSerializer, DepartmentSerializer, MedicalNoteSerializer, DoctorAvailabilitySerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    # los actions ayudan a definir acciones personalizadas en el viewset
    # para usar un action, se va a URL /api/doctors/doctors/<pk>/set_on_vacation/ y en la vista de django que aparece hay que dar click en el boton "POST" para ejecutar la acción
    @action(detail=True, methods=['post'], url_path='set-on-vacation') # detail=True indica que la acción es para un objeto específico
    def set_on_vacation(self, request, pk=None):
        """Set a doctor on vacation."""
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({'status': 'doctor set on vacation'})

    @action(detail=True, methods=['post'], url_path='set-off-vacation')
    def set_off_vacation(self, request, pk=None):
        """Set a doctor off vacation."""
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({'status': 'doctor set off vacation'})

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializer

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer