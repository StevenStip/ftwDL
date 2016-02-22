# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_interfae', '0002_auto_20151020_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fling',
            old_name='fling_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='sender',
            old_name='sender_id',
            new_name='id',
        ),
        migrations.AddField(
            model_name='sender',
            name='first_name',
            field=models.CharField(default='john doe', max_length=250),
            preserve_default=False,
        ),
    ]
