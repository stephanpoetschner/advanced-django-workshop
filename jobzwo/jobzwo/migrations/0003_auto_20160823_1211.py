# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobzwo', '0002_auto_20160823_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
