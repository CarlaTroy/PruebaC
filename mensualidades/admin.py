from django.contrib import admin

# Register your models here.
from mensualidades.models import Course, Student, Enrollment, Cohort, Payment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_names", "first_names", "identification")
    search_fields = ("last_names", "first_names", "identification")


class EnrollmentInline(admin.TabularInline):
    model = Enrollment


@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ("course", "name", "initial_date", "end_date")
    inlines = (EnrollmentInline,)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "cohort")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("enrollment", "payment_date")
