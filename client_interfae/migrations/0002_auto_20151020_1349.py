# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_interfae', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fling',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sender',
            name='id',
        ),
        migrations.AlterField(
            model_name='fling',
            name='created_at',
            field=models.DateTimeField(verbose_name=b'created at'),
        ),
        migrations.AlterField(
            model_name='fling',
            name='fling_id',
            field=models.CharField(max_length=250, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='sender',
            name='sender_id',
            field=models.CharField(max_length=250, serialize=False, primary_key=True),
        ),
    ]
