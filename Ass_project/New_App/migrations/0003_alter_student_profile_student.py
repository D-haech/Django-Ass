# Generated by Django 5.1.2 on 2024-10-27 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_App', '0002_program_student_student_profile_delete_portal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_profile',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='New_App.student'),
        ),
    ]
