from rest_framework.routers import DefaultRouter # crea las viewsets que nos dan acceso a unas rutas
from django.urls import path
from .views import DoctorView, DoctorDetailView
from .viewsets import DoctorViewSet, DepartmentViewSet, MedicalNoteViewSet, DoctorAvailabilityViewSet

router = DefaultRouter() 
router.register(r"doctors", DoctorViewSet)  # el primer argumento es un prefijo para las rutas, el segundo es la vista que maneja las operaciones CRUD
router.register(r"departments", DepartmentViewSet)
router.register(r"medical_notes", MedicalNoteViewSet)
router.register(r"doctor_availabilities", DoctorAvailabilityViewSet)

urlpatterns = [
# path("", DoctorView.as_view()), # Use as_view() to convert the class-based view into a callable view
# path("<int:pk>/", DoctorDetailView.as_view()),  # Use DoctorDetailView for detail views
] + router.urls  # el router.urls nos retorna una lista de rutas que se van a unir con la lista de urlpatterns

# urlpatterns += router.urls  # esta forma es equivalente a la anterior
