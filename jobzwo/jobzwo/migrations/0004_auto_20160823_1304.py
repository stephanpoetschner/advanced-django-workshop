# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobzwo', '0003_auto_20160823_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('active', 'active'), ('inactive', 'inactive')], max_length=10),
        ),
    ]
