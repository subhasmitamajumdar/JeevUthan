# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('ngo_id', models.AutoField(serialize=False, primary_key=True)),
                ('ngo_name', models.CharField(max_length=200)),
                ('ngo_address', models.CharField(max_length=200)),
                ('ngo_contact_no1', models.CharField(max_length=20)),
                ('ngo_contact_no2', models.CharField(max_length=20)),
                ('ngo_contact_no3', models.CharField(max_length=20)),
                ('ngo_location_id', models.IntegerField()),
                ('ngo_email', models.CharField(max_length=100)),
                ('ngo_website', models.CharField(max_length=100)),
            ],
        ),
    ]
