from django.db import models


# Create your models here.
class Student(models.Model):
    last_names = models.CharField(max_length=150, verbose_name="Apellidos")
    first_names = models.CharField(max_length=150, verbose_name="Nombres")
    identification = models.CharField(max_length=13, verbose_name="Cédula")
    cellphone = models.CharField(max_length=15, verbose_name="Celular")
    address = models.CharField(max_length=300, verbose_name="Dirección")
    email = models.EmailField(max_length=150)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "4. Estudiantes"

    def __str__(self):
        return f"{self.last_names} {self.first_names}"
