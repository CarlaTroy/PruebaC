# Generated by Django 4.1.3 on 2022-12-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mensualidades", "0007_enrollment_discount_enrollment_payment_day_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="enrollment",
            name="initial_payment",
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="discount",
            field=models.FloatField(default=0, verbose_name="Descuento"),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="payment_day",
            field=models.PositiveIntegerField(verbose_name="Día de Pago"),
        ),
    ]