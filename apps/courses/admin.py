from django.contrib import admin

# Register your models here.
from apps.courses.models import Course, Cohort
from apps.enrollment.models import Enrollment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class EnrollmentInline(admin.TabularInline):
    model = Enrollment


@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ("course", "name", "initial_date", "end_date")
    inlines = (EnrollmentInline,)
