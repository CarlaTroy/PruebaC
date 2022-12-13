import calendar
from datetime import date

from dateutil.relativedelta import *
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.courses.models import Cohort
from apps.student.models import Student


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
    CHOICE_STATUS = ((True, "PAGADO"), (False, "NO PAGADO"))
    amount = models.FloatField()
    payment_date = models.DateField()
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="payments_enrollment")
    status = models.BooleanField(default=False, verbose_name="Pagado", choices=CHOICE_STATUS)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "5. Pagos"

    def __str__(self):
        return f"{self.enrollment.student}"
