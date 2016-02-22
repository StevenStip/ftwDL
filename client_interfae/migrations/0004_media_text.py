# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_interfae', '0003_auto_20151020_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='text',
            field=models.CharField(default='notext', max_length=250),
            preserve_default=False,
        ),
    ]
