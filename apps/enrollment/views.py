# Create your views here.
import datetime

from django.db.models import Count, Q
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from apps.courses.models import Cohort
from apps.enrollment.models import Enrollment, Payment


class IndexView(TemplateView):
    template_name = "base/index.html"


# MATRICULAR

class EnrollmentCreateView(CreateView):
    template_name = "apps/enrollment/create.html"
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
    template_name = "apps/enrollment/create.html"
    model = Enrollment
    fields = ("student", "cohort", "dues_number", "discount", "initial_payment", "payment_day")
    success_url = reverse_lazy('course_list')


class EnrollmentListView(ListView):
    template_name = "apps/enrollment/list.html"
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
    template_name = "apps/payments/list.html"

    def get_queryset(self):
        return Payment.objects.filter(enrollment__pk=self.kwargs['pk'])


class ReceivePayment(UpdateView):
    model = Payment
    template_name = "apps/payments/receive_payment.html"
    fields = ("status",)

    def get_success_url(self):
        return reverse_lazy('payment_list', kwargs={'pk': self.object.enrollment.pk})
