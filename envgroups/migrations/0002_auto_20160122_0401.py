# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='category',
            field=models.CharField(max_length=2, choices=[(b'FO', b'Food'), (b'SO', b'Social'), (b'EN', b'Energy'), (b'AC', b'Activism'), (b'EV', b'Environment'), (b'PR', b'Projects'), (b'AR', b'Arts'), (b'ED', b'Education'), (b'PO', b'Policy')]),
        ),
    ]
