# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('register_for_pet', '0006_auto_20150919_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_breed',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z][^A-Z]*', message=b'name should contain only characters')]),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_colour',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z][^A-Z]*', message=b'name should contain only characters')]),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_missing_loc',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z][^A-Z]*', message=b'name should contain only characters')]),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z][^A-Z]*', message=b'name should contain only characters')]),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(max_length=30, choices=[(b'DOG', b'Dog'), (b'CAT', b'Cat'), (b'OTHER', b'Other')], validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z][^A-Z]*', message=b'name should contain only characters')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z][^A-Z]', message=b'name should contain only characters')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z][^A-Z]', message=b'name should contain only characters')]),
        ),
    ]
