from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    # para agregar validaciones personalizadas, se pueden definir métodos que comiencen con "validate_" seguido del nombre del campo
    def validate_email(self, value):
        """Validate that the email ends with @gmail.com."""
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError("Email must end with @gmail.com")
        return value
    
    # para validar múltiples campos, se puede definir el método validate sin el prefijo del campo
    def validate(self, attrs):
        """Validate that the doctor has a valid phone number and qualification."""
        if len(attrs.get('phone_number', '')) < 10:
            raise serializers.ValidationError("Phone number must be at least 10 digits long.")
        if not attrs.get('qualification'):
            raise serializers.ValidationError("Qualification is required.")
        return attrs

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'

class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'
