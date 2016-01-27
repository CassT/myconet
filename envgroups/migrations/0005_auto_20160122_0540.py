# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0004_auto_20160122_0539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='health',
            new_name='wellness',
        ),
    ]
