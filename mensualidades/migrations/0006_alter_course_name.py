# Generated by Django 4.1.3 on 2022-11-27 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mensualidades", "0005_alter_enrollment_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="name",
            field=models.CharField(max_length=100, unique=True, verbose_name="Nombre"),
        ),
    ]