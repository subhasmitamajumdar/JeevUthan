# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150913_1137'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
    ]
