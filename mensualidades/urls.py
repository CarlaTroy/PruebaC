from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mensualidades import views

urlpatterns = [
                  path("", views.IndexView.as_view()),
                  path("estudiante/crear", views.StudentCreateView.as_view(), name="student_create"),
                  path("estudiante/actualizar/<int:pk>", views.StudentUpdateView.as_view(), name="student_update"),
                  path("estudiante/listar", views.StudentListView.as_view(), name="student_list"),
                  # course
                  path("curso/crear", views.CourseCreateView.as_view(), name="course_create"),
                  path("curso/actualizar/<int:pk>", views.CourseUpdateView.as_view(), name="course_update"),
                  path("curso/listar", views.CourseListView.as_view(), name="course_list"),
                  # enrollment
                  path("matricula/crear", views.EnrollmentCreateView.as_view(), name="enrollment_create"),
                  path("matricula/actualizar/<int:pk>", views.EnrollmentUpdateView.as_view(), name="enrollment_update"),
                  path("matricula/listar", views.EnrollmentListView.as_view(), name="enrollment_list"),
                  # payments
                  path("matricula/pensiones/<int:pk>", views.PaymentListView.as_view(), name="payment_list"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
