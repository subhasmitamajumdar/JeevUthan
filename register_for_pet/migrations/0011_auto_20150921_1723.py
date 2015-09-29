# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('register_for_pet', '0010_auto_20150920_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_height',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'[0-9]*', message=b'invalid height')]),
        ),
    ]
