# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pet_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'[a-z]*', message=b'name should contain only characters')])),
                ('pet_height', models.CharField(unique=b'True', max_length=15, validators=[django.core.validators.RegexValidator(regex=b'[0-9]*', message=b'invalid height')])),
                ('pet_colour', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'[a-z]*', message=b'name should contain only characters')])),
                ('pet_breed', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'[a-z]*', message=b'name should contain only characters')])),
                ('pet_missing_date', models.DateTimeField()),
                ('pet_missing_loc', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'[a-z]*', message=b'name should contain only characters')])),
                ('pet_type', models.CharField(max_length=30, choices=[(b'DOG', b'Dog'), (b'CAT', b'Cat'), (b'OTHER', b'Other')], validators=[django.core.validators.RegexValidator(regex=b'[a-z]*', message=b'name should contain only characters')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'[a-z]*', message=b'name should contain only characters')])),
                ('lastname', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'[a-z]*', message=b'name should contain only characters')])),
                ('email', models.EmailField(unique=True, max_length=100, validators=[django.core.validators.RegexValidator(regex=b'^[\\w\\.-]+@[a-z]+\\.(([a-z]{2,3})|(\\.([a-z]?)))\\b', message=b'inavalid email format')])),
                ('contact', models.CharField(max_length=15, unique=True, null=True, validators=[django.core.validators.RegexValidator(regex=b'[0-9]*', message=b'invalid contact')])),
            ],
        ),
    ]
