# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='username',
            field=models.CharField(max_length=100, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='vet',
            name='username',
            field=models.CharField(max_length=100, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='ngo_email',
            field=models.EmailField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[\\w\\.-]+@[a-z]+\\.(([a-z]{2,3})|(\\.([a-z]?)))\\b', message=b'inavalid email format')]),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='ngo_name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]$', message=b'name should contain only characters')]),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='ngo_website',
            field=models.URLField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterModelTable(
            name='ngo',
            table=None,
        ),
        migrations.AlterModelTable(
            name='vet',
            table=None,
        ),
    ]
