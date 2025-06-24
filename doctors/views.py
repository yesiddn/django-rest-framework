from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor 
from .serializers import DoctorSerializer 

class DoctorView(APIView): # APIView es una clase base para crear vistas de API RESTful en Django REST Framework, parecida al decorador @api_view
    """
    View to handle doctor-related operations.
    """
    # The allowed HTTP methods are determined by the methods defined in this class (get, post, etc.)

    def get(self, request):
        """
        Handle GET requests for doctors.
        """
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Handle POST requests to create a new doctor.
        """
        serializer = DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor = serializer.save()
        return Response(DoctorSerializer(doctor).data, status=status.HTTP_201_CREATED)

class DoctorDetailView(APIView):
    """
    View to handle operations on a specific doctor.
    """

    def get_object(self, pk):
        """
        Retrieve a doctor by primary key (pk).
        """
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return None

    def get(self, request, pk):
        """
        Handle GET requests for a specific doctor.
        """
        doctor = self.get_object(pk)
        if not doctor:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Handle PUT requests to update a specific doctor.
        """
        doctor = self.get_object(pk)
        if not doctor:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorSerializer(doctor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        """
        Handle DELETE requests to remove a specific doctor.
        """
        doctor = self.get_object(pk)
        if not doctor:
            return Response(status=status.HTTP_404_NOT_FOUND)

        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    