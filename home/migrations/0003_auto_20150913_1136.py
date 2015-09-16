# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150907_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='loc_name',
            new_name='location_name',
        ),
        migrations.AlterModelTable(
            name='location',
            table='wp_ju_location',
        ),
    ]
