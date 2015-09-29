# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150927_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='ngo_address',
            field=models.TextField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='ngo_name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z ]+$', message=b'name should contain only characters')]),
        ),
        migrations.AlterField(
            model_name='vet',
            name='vet_address',
            field=models.TextField(unique=True, max_length=200),
        ),
    ]
