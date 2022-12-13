from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.courses import views

urlpatterns = [
                  path("curso/crear", views.CourseCreateView.as_view(), name="course_create"),
                  path("curso/actualizar/<int:pk>", views.CourseUpdateView.as_view(), name="course_update"),
                  path("curso/listar", views.CourseListView.as_view(), name="course_list"),
                  # cohort
                  path("cohorte/crear", views.CohortCreateView.as_view(), name="cohort_create"),
                  path("cohorte/actualizar/<int:pk>", views.CohortUpdateView.as_view(), name="cohort_update"),
                  path("cohorte/listar", views.CohortListView.as_view(), name="cohort_list"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
