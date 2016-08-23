# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobzwo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_hearing_impairment_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='is_motor_impairment_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='is_visual_impairment_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
