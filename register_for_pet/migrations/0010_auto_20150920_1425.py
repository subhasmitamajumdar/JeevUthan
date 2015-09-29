# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('register_for_pet', '0009_auto_20150919_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=100, null=True, validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z][^A-Z]*$', message=b'name should contain only characters')]),
        ),
    ]
