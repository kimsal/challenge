# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-17 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import my_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20180816_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='my_app.School'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_identification',
            field=models.CharField(default=my_app.models.getUniqueString, max_length=20, unique=True),
        ),
    ]