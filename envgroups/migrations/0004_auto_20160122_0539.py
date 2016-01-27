# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0003_auto_20160122_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='activism',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='arts',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='education',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='energy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='environment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='food',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='health',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='policy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='projects',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='social',
            field=models.BooleanField(default=False),
        ),
    ]
