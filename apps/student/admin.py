from django.contrib import admin

# Register your models here.
from apps.student.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_names", "first_names", "identification")
    search_fields = ("last_names", "first_names", "identification")
