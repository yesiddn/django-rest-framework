from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord

class PatientSerializer(serializers.ModelSerializer):
  # Meta especifica la configuración del serializador
  # model indica el modelo que se va a serializar
  # fields indica los campos que se incluirán en la serialización
  class Meta:
      model = Patient
      fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
  class Meta:
      model = Insurance
      fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
  class Meta:
      model = MedicalRecord
      fields = '__all__'