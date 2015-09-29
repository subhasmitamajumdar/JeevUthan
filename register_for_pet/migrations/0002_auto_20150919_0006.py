# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register_for_pet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=30, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_missing_date',
            field=models.DateField(),
        ),
    ]
