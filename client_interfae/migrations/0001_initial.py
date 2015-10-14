# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fling_id', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField()),
                ('country', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=500)),
                ('local_path', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_id', models.CharField(max_length=250)),
                ('jid', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='fling',
            name='media',
            field=models.ForeignKey(to='client_interfae.Media'),
        ),
        migrations.AddField(
            model_name='fling',
            name='sender',
            field=models.ForeignKey(to='client_interfae.Sender'),
        ),
    ]
