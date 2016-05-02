# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0007_comment_groupposting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('tagline', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=200)),
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
                ('wdywtd', models.TextField()),
                ('needs', models.TextField()),
                ('offerings', models.TextField()),
                ('ideal_collaboration', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collaborator', models.CharField(max_length=200)),
                ('seeking_help', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='housing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='research',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group',
            name='housing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group',
            name='research',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='gtype',
            field=models.CharField(max_length=2, choices=[(b'SG', b'Academic'), (b'FP', b'For Profit'), (b'NP', b'Non Profit')]),
        ),
    ]
