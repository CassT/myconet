# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0010_auto_20160310_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='other_interests',
            field=models.CharField(max_length=200),
        ),
    ]
