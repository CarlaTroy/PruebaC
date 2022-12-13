from django.contrib import admin

# Register your models here.
from apps.enrollment.models import Enrollment, Payment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "cohort")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("enrollment", "payment_date")
