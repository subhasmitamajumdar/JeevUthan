# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20150914_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='ngo_email',
            field=models.EmailField(max_length=100, blank=True),
        ),
    ]
