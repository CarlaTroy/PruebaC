# Generated by Django 4.1.3 on 2022-12-04 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mensualidades", "0009_payment_status_alter_enrollment_dues_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="enrollment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="payments_enrollment",
                to="mensualidades.enrollment",
            ),
        ),
    ]