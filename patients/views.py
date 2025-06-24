from django.shortcuts import render
from rest_framework.response import Response # esta clase se usa para enviar respuestas HTTP y formatear los datos de respuesta en JSON
from rest_framework.decorators import api_view # api_view es un decorador que permite definir vistas de API RESTful
from rest_framework import status # este módulo proporciona constantes para los códigos de estado HTTP
from .serializers import PatientSerializer
from .models import Patient

# @api_view(['GET']) # este decorador indica que la vista acepta solicitudes GET
def list_patients(request):
  """
  View to list all patients.
  """
  patients = Patient.objects.all() 
  serializer = PatientSerializer(patients, many=True) # many=True indica que se están serializando múltiples instancias
  return Response(serializer.data) # devuelve los datos serializados como respuesta HTTP en formato JSON

# @api_view(['POST'])
def create_patient(request):
    """
    View to create a new patient.
    """
    serializer = PatientSerializer(data=request.data)
    
    # se quita el condicional ya que raise_exception retorna el bad request y por ende no se ejecuta el resto del código
    serializer.is_valid(raise_exception=True) # con raise_exception=True, si los datos no son válidos, se lanzará una excepción y se devolverá un error 400 Bad Request automáticamente

    serializer.save() # guarda el nuevo paciente en la base de datos
    return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201 Created
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 400 Bad Request

@api_view(['GET', 'POST'])
def patient(request):
  """
  View to handle patient creation and listing.
  """
  if request.method == 'GET':
      return list_patients(request)
  elif request.method == 'POST':
      return create_patient(request)
  
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def patient_detail(request, pk):
    """
    View to handle patient detail retrieval, update, and deletion.
    """
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = PatientSerializer(patient, data=request.data, partial=True) # partial=True permite actualizar solo algunos campos
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
