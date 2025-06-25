from rest_framework import serializers
from .models import Appointment, MedicalNote

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

