# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150914_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='ngo_contact_no2',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='ngo_contact_no3',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='ngo_email',
            field=models.EmailField(unique=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='ngo_website',
            field=models.URLField(max_length=100, blank=True),
        ),
    ]
