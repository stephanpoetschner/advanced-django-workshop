# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_job_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='company_name',
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.ForeignKey(default=1, to='jobs.Company'),
            preserve_default=False,
        ),
    ]
