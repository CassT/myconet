# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0006_auto_20160128_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('top_level', models.BooleanField()),
                ('parentid', models.IntegerField()),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GroupPosting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupid', models.IntegerField()),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]
