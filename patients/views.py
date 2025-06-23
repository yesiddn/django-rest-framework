from django.shortcuts import render
from rest_framework.response import Response # esta clase se usa para enviar respuestas HTTP y formatear los datos de respuesta en JSON
from rest_framework.decorators import api_view # api_view es un decorador que permite definir vistas de API RESTful
from .serializers import PatientSerializer
from .models import Patient

@api_view(['GET']) # este decorador indica que la vista acepta solicitudes GET
def list_patients(request):
  """
  View to list all patients.
  """
  patients = Patient.objects.all() 
  serializer = PatientSerializer(patients, many=True) # many=True indica que se están serializando múltiples instancias
  return Response(serializer.data) # devuelve los datos serializados como respuesta HTTP en formato JSON

@api_view(['POST'])
def create_patient(request):
    """
    View to create a new patient.
    """
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() # guarda el nuevo paciente en la base de datos
        return Response(serializer.data, status=201)  # 201 Created
    return Response(serializer.errors, status=400)  # 400 Bad Request
