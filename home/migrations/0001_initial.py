# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(serialize=False, primary_key=True)),
                ('location_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('ngo_id', models.AutoField(serialize=False, primary_key=True)),
                ('ngo_name', models.CharField(unique=True, max_length=200)),
                ('ngo_address', models.CharField(unique=True, max_length=200)),
                ('ngo_contact_no1', models.CharField(blank=True, unique=True, max_length=20, validators=[django.core.validators.RegexValidator(regex=b'\\+[0-9\\-()]*', message=b'invalid contact')])),
                ('ngo_contact_no2', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex=b'\\+[0-9\\-()]*', message=b'invalid contact')])),
                ('ngo_contact_no3', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex=b'\\+[0-9\\-()]*', message=b'invalid contact')])),
                ('ngo_location_id', models.IntegerField()),
                ('ngo_email', models.EmailField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(regex=b'^[\\w\\.-]+@[a-z]+\\.(([a-z]{2,3})|(\\.([a-z]?)))\\b', message=b'inavalid email format')])),
                ('ngo_website', models.URLField(max_length=100, blank=True)),
                ('password', models.CharField(max_length=30, unique=True, null=True)),
            ],
            options={
                'db_table': 'Ngo',
            },
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('vet_id', models.AutoField(serialize=False, primary_key=True)),
                ('vet_name', models.CharField(max_length=200)),
                ('vet_address', models.CharField(unique=True, max_length=200)),
                ('vet_clinic_no', models.CharField(max_length=20, blank=True)),
                ('vet_mobile_no1', models.CharField(max_length=20, blank=True)),
                ('vet_mobile_no2', models.CharField(max_length=20, blank=True)),
                ('vet_location_id', models.IntegerField()),
                ('vet_email', models.EmailField(blank=True, max_length=100, validators=[django.core.validators.RegexValidator(regex=b'^[\\w\\.-]+@[a-z]+\\.(([a-z]{2,3})|(\\.([a-z]?)))\\b', message=b'inavalid email format')])),
                ('vet_website', models.URLField(max_length=100, blank=True)),
                ('password', models.CharField(max_length=30, unique=True, null=True)),
            ],
            options={
                'db_table': 'Vet',
            },
        ),
    ]
