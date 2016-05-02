# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0008_auto_20160309_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='other_interests',
            field=models.BooleanField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='gtype',
            field=models.CharField(max_length=2, choices=[(b'SG', b'Academic'), (b'FP', b'Business'), (b'NP', b'Non Profit'), (b'GV', b'Government'), (b'UC', b'Unclassified')]),
        ),
    ]
