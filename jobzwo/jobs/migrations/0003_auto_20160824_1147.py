# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20160822_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_hearing_impairment_accepted',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_motor_impairment_accepted',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_visual_impairment_accepted',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(editable=False, max_length=254, choices=[('DRAFT', 'Draft'), ('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='DRAFT'),
        ),
    ]
