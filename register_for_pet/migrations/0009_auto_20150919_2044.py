# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register_for_pet', '0008_auto_20150919_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(max_length=30, choices=[(b'DOG', b'Dog'), (b'CAT', b'Cat'), (b'OTHER', b'Other')]),
        ),
    ]
