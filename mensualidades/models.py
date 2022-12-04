import calendar
from datetime import date

from dateutil.relativedelta import *
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Estudiante")
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, verbose_name="Cohorte")
    dues_number = models.PositiveIntegerField(verbose_name="Cuotas")
    initial_payment = models.FloatField(verbose_name="Pago Inicial", default=0)
    payment_day = models.PositiveIntegerField(verbose_name="Día de Pago")
    discount = models.FloatField(default=0, verbose_name="Descuento")
    balance = models.FloatField("Saldo pendiente", blank=True, null=True)

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "3. Matrículas"
        unique_together = ("student", "cohort")

    def __str__(self):
        return f"{self.student.last_names} {self.student.first_names}"


@receiver(post_save, sender=Enrollment)
def my_handler(sender, **kwargs):
    initial_payment = kwargs['instance'].initial_payment
    effective_cost = kwargs['instance'].cohort.effective_cost
    if initial_payment != effective_cost:
        credit_cost = kwargs['instance'].cohort.credit_cost
        dues_number = kwargs['instance'].dues_number
        discount = kwargs['instance'].discount
        discount = credit_cost * discount / 100
        payment_day = kwargs['instance'].payment_day
        amount = round((credit_cost - discount - initial_payment) / dues_number, 2)
        for i in range(1, dues_number + 1):

            payment_date = date.today()
            try:
                payment_date = payment_date.replace(day=payment_day)
                payment_date = payment_date + relativedelta(months=+i)
            except:
                payment_date = payment_date + relativedelta(months=+i)
                calendar.monthrange(payment_date.year, payment_date.month)[1]
                payment_date = payment_date.replace(day=payment_day)

            Payment.objects.create(amount=amount, payment_date=payment_date, enrollment=kwargs['instance'])


class Payment(models.Model):
    amount = models.FloatField()
    payment_date = models.DateField()
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="payments_enrollment")
    status = models.BooleanField(default=False, verbose_name="Pagado")

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "5. Pagos"

    def __str__(self):
        return f"{self.enrollment.student}"
