from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.student import views

urlpatterns = [
                  path("estudiante/crear", views.StudentCreateView.as_view(), name="student_create"),
                  path("estudiante/actualizar/<int:pk>", views.StudentUpdateView.as_view(), name="student_update"),
                  path("estudiante/listar", views.StudentListView.as_view(), name="student_list"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
