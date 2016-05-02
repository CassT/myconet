# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0014_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food', models.BooleanField(default=False)),
                ('social', models.BooleanField(default=False)),
                ('energy', models.BooleanField(default=False)),
                ('activism', models.BooleanField(default=False)),
                ('environment', models.BooleanField(default=False)),
                ('projects', models.BooleanField(default=False)),
                ('arts', models.BooleanField(default=False)),
                ('education', models.BooleanField(default=False)),
                ('policy', models.BooleanField(default=False)),
                ('wellness', models.BooleanField(default=False)),
                ('housing', models.BooleanField(default=False)),
                ('research', models.BooleanField(default=False)),
                ('tools', models.BooleanField(default=False)),
                ('two', models.BooleanField(default=False)),
                ('three', models.BooleanField(default=False)),
                ('uno', models.BooleanField(default=False)),
                ('dose', models.BooleanField(default=False)),
                ('tres', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('collaborator', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=200)),
                ('seeking_help', models.CharField(max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('help_text', models.TextField()),
                ('ptype', models.CharField(max_length=2, choices=[(b'SG', b'Academic'), (b'FP', b'Business'), (b'NP', b'Non Profit'), (b'GV', b'Government'), (b'UC', b'Unclassified')])),
                ('link', models.CharField(max_length=300)),
                ('connections', models.TextField()),
            ],
        ),
    ]
