from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.enrollment import views

urlpatterns = [
                  path("", views.IndexView.as_view()),

                  # course

                  # enrollment
                  path("matricula/crear", views.EnrollmentCreateView.as_view(), name="enrollment_create"),
                  path("matricula/actualizar/<int:pk>", views.EnrollmentUpdateView.as_view(), name="enrollment_update"),
                  path("matricula/listar", views.EnrollmentListView.as_view(), name="enrollment_list"),
                  # payments
                  path("matricula/pensiones/<int:pk>", views.PaymentListView.as_view(), name="payment_list"),
                  path("matricula/recibir_pago/<int:pk>", views.ReceivePayment.as_view(), name="receive_payment"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
