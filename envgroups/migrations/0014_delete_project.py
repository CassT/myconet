# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0013_auto_20160403_2245'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Project',
        ),
    ]
