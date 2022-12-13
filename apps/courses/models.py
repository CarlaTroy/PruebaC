from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre", unique=True)
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", blank=True, null=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "1. Cursos"

    def __str__(self):
        return self.name


class Cohort(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Curso")
    name = models.CharField(max_length=150, verbose_name="Nombre de la Cohorte")
    initial_date = models.DateField(verbose_name="Fecha de Inicio")
    end_date = models.DateField(verbose_name="Fecha fin")
    effective_cost = models.FloatField(verbose_name="Costo en efectivo")
    credit_cost = models.FloatField(verbose_name="Costo a crédito")

    class Meta:
        verbose_name = "Cohorte"
        verbose_name_plural = "2. Cohortes"

    def __str__(self):
        return f"{self.course} {self.name}"
