# Generated by Django 5.1.4 on 2025-01-16 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0003_alter_doctor_mobile_alter_patient_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='gendar',
            new_name='gender',
        ),
    ]
