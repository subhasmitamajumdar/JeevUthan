# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('register_for_pet', '0002_auto_20150919_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'[a-z]*[^A-Z]', message=b'name should contain only characters')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(regex=b'[a-z]*[^A-Z]', message=b'name should contain only characters')]),
        ),
    ]
