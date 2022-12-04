# Create your views here.
import datetime

from django.db.models import Count, Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from mensualidades.models import Student, Course, Enrollment, Cohort, Payment


class IndexView(TemplateView):
    template_name = "index.html"


class StudentCreateView(CreateView):
    template_name = "students/create.html"
    model = Student
    fields = "__all__"
    success_url = reverse_lazy('student_list')


class StudentUpdateView(UpdateView):
    template_name = "students/create.html"
    model = Student
    fields = "__all__"
    success_url = reverse_lazy('student_list')


class StudentListView(ListView):
    template_name = "students/list.html"
    queryset = Student.objects.all()


# CURSOS

class CourseCreateView(CreateView):
    template_name = "course/create.html"
    model = Course
    fields = "__all__"
    success_url = reverse_lazy('course_list')


class CourseUpdateView(UpdateView):
    template_name = "course/create.html"
    model = Course
    fields = "__all__"
    success_url = reverse_lazy('course_list')


class CourseListView(ListView):
    template_name = "course/list.html"
    queryset = Course.objects.all()


# MATRICULAR

class EnrollmentCreateView(CreateView):
    template_name = "enrollment/create.html"
    model = Enrollment
    fields = ("student", "cohort", "dues_number", "discount", "initial_payment", "payment_day")
    success_url = reverse_lazy('enrollment_list')

    def get(self, request, *args, **kwargs):
        self.object = None
        if "ajaxcourse" in request.GET:
            cohort_id = request.GET['value']
            queryset = Cohort.objects.filter(pk=cohort_id).values()
            return JsonResponse({"results": list(queryset)})
        return super().get(request, *args, **kwargs)


class EnrollmentUpdateView(UpdateView):
    template_name = "enrollment/create.html"
    model = Enrollment
    fields = ("student", "cohort", "dues_number", "discount", "initial_payment", "payment_day")
    success_url = reverse_lazy('course_list')


class EnrollmentListView(ListView):
    template_name = "enrollment/list.html"
    queryset = Enrollment.objects.all()

    def get_queryset(self):
        return Enrollment.objects.all().annotate(
            pending_payments=Count(
                'payments_enrollment',
                filter=Q(payments_enrollment__status=False),
                distinct=True
            )).annotate(
            late_payments=Count(
                'payments_enrollment',
                filter=(
                        Q(payments_enrollment__payment_date__lt=datetime.datetime.now()) & Q(
                    payments_enrollment__status=False)),
                distinct=True
            ))


class PaymentListView(ListView):
    template_name = "payments/list.html"

    def get_queryset(self):
        return Payment.objects.filter(enrollment__pk=self.kwargs['pk'])
