# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('location', models.TextField()),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=1, choices=[(b'F', b'Food'), (b'S', b'Social'), (b'E', b'Energy'), (b'A', b'Activism')])),
                ('title', models.CharField(max_length=200)),
                ('mission', models.TextField()),
                ('employees', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('products', models.TextField()),
                ('hiring', models.CharField(max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('hiring_text', models.TextField()),
                ('gtype', models.CharField(max_length=2, choices=[(b'SG', b'Student Group'), (b'FP', b'For Profit'), (b'NP', b'Non Profit')])),
                ('link', models.CharField(max_length=300)),
                ('connections', models.TextField()),
            ],
        ),
    ]
