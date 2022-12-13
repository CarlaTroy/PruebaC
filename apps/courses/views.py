# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from apps.courses.models import Course, Cohort


class CourseCreateView(CreateView):
    template_name = "apps/course/create.html"
    model = Course
    fields = "__all__"
    success_url = reverse_lazy('course_list')


class CourseUpdateView(UpdateView):
    template_name = "apps/course/create.html"
    model = Course
    fields = "__all__"
    success_url = reverse_lazy('course_list')


class CourseListView(ListView):
    template_name = "apps/course/list.html"
    queryset = Course.objects.all()


# COHORTE

class CohortCreateView(CreateView):
    template_name = "apps/course/create.html"
    model = Cohort
    fields = "__all__"
    success_url = reverse_lazy('cohort_list')


class CohortUpdateView(UpdateView):
    template_name = "apps/course/create.html"
    model = Cohort
    fields = "__all__"
    success_url = reverse_lazy('cohort_list')


class CohortListView(ListView):
    template_name = "apps/course/list.html"
    queryset = Cohort.objects.all()
