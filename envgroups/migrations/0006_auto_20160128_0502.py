# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0005_auto_20160122_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='activism',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='arts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='education',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='energy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='environment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='food',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='policy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='projects',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='social',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='wellness',
            field=models.BooleanField(default=False),
        ),
    ]
