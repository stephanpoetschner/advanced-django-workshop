# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20160824_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(max_length=254, default='Google'),
            preserve_default=False,
        ),
    ]
