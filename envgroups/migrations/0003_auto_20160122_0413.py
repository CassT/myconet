# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0002_auto_20160122_0401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='category',
        ),
        migrations.AddField(
            model_name='group',
            name='activism',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='group',
            name='arts',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='group',
            name='education',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='group',
            name='energy',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='group',
            name='environment',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='group',
            name='food',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='group',
            name='health',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='group',
            name='policy',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='group',
            name='projects',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='group',
            name='social',
            field=models.NullBooleanField(),
        ),
    ]
