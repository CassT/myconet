# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envgroups', '0016_auto_20160405_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Acupuncture',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Animal_Husbandry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Aquaponics_Hydroponics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Art_Supplies',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Audio_Video_Engineering',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Automotive_Maintenance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Bodywork_Breathwork',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Children_Programs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Community_Space',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Compost_Manure_Mulch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Composting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Construction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Construction_Materials_Electrical',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Construction_Materials_Finishing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Construction_Materials_Plumbing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Construction_Materials_Structural',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Cooking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Dance_Performance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Digital_Media',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Disruptive_Action',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Domestic_Animals',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Earthmoving_Equipment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Energy_Generation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Energy_Installation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Facilitation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Gardening',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Grant_Writing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Green_Building',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Herbal_Medicine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Journalism',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Land_Agriculture',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Land_Housing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Legal_Defense',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Legal_Regulations',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Lights',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Local_Community_Knowledge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Local_Ecology_Knowledge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Manual_Labor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Money',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Music',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Painting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Photography',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Planning_Coordination',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Plant_Starts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Pots',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Promoting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Sculpture',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Seeds',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Site_Planning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Sound_Healing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Teaching',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Tools_Art',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Tools_Construction',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Tools_Farming',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Vehicle',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='Web_Development',
            field=models.BooleanField(default=False),
        ),
    ]
