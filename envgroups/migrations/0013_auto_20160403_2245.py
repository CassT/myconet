# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0012_auto_20160311_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='value',
        ),
        migrations.AddField(
            model_name='project',
            name='dose',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='one',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='three',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='tres',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='two',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='uno',
            field=models.BooleanField(default=False),
        ),
    ]
