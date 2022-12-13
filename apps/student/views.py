# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from apps.student.models import Student


class StudentCreateView(CreateView):
    template_name = "apps/students/create.html"
    model = Student
    fields = "__all__"
    success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    template_name = "apps/students/create.html"
    model = Student
    fields = "__all__"
    success_url = reverse_lazy('student_list')


class StudentListView(ListView):
    template_name = "apps/students/list.html"
    queryset = Student.objects.all()
