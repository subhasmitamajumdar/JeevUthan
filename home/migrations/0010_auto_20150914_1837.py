# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_ngo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='ngo_email',
            field=models.EmailField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='ngo_website',
            field=models.URLField(max_length=100),
        ),
    ]
