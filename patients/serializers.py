from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer

class PatientSerializer(serializers.ModelSerializer):
  appointments = AppointmentSerializer(many=True, read_only=True) # many=True indica que se espera una lista de objetos Appointment, read_only=True indica que este campo no se puede modificar a través del serializador

  # Meta especifica la configuración del serializador
  # model indica el modelo que se va a serializar
  # fields indica los campos que se incluirán en la serialización
  class Meta:
      model = Patient
      fields = [
        'id',  # Incluye el campo id para identificar al paciente
        'first_name',
        'last_name',
        'date_of_birth',
        'contact_number',
        'email',
        'address',
        'medical_history',
        'appointments',  # Incluye las citas relacionadas -> de esta forma al  hacer un GET a /patients/ se incluirán las citas del paciente
      ]

class InsuranceSerializer(serializers.ModelSerializer):
  class Meta:
      model = Insurance
      fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
  class Meta:
      model = MedicalRecord
      fields = '__all__'