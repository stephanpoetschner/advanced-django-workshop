# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('titel', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=30)),
                ('external_url', models.URLField()),
                ('contact_email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('status', models.CharField(choices=[('d', 'draft'), ('a', 'active'), ('i', 'inactive')], max_length=1)),
            ],
        ),
    ]
