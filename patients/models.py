from django.db import models

class Patient(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  date_of_birth = models.DateField()
  contact_number = models.CharField(max_length=15)
  email = models.EmailField(unique=True)
  address = models.TextField()
  medical_history = models.TextField(blank=True, null=True)

class Insurance(models.Model):
  patient = models.ForeignKey(
      Patient,
      related_name="insurances",
      on_delete=models.CASCADE,
      # class, nombre que se le da a la relación inversa, acción al eliminar una instancia de Patient
      # related_name especifica el nombre que se usará para acceder a los objetos relacionados desde el modelo referenciado. Esto significa que, desde una instancia de Patient, puedes acceder a todos sus seguros (Insurance) usando patient.insurances.all(). Sin related_name, el nombre por defecto sería insurance_set.
  )
  provider = models.CharField(max_length=100)
  policy_number = models.CharField(max_length=100, unique=True)
  expiration_date = models.DateField()

class MedicalRecord(models.Model):
  patient = models.ForeignKey(
    Patient, related_name='medical_records', on_delete=models.CASCADE
  )
  date = models.DateField()
  diagnosis = models.TextField()
  treatment = models.TextField()
  follow_up_date = models.DateField(blank=True, null=True) # blank permite que el campo esté vacío
