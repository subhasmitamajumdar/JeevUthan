# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_location'),
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
    ]
