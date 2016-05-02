# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0011_auto_20160310_0445'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPosting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupid', models.IntegerField()),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='activism',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='arts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='connections',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='education',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='energy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='environment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='food',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='help_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='housing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='policy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='projects',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='ptype',
            field=models.CharField(default='', max_length=2, choices=[(b'SG', b'Academic'), (b'FP', b'Business'), (b'NP', b'Non Profit'), (b'GV', b'Government'), (b'UC', b'Unclassified')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='research',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='social',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='summary',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='value',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='wellness',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='collaborator',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='seeking_help',
            field=models.CharField(max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
        ),
    ]
