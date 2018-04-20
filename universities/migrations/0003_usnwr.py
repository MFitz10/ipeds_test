# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_degreesbyageethnicity_degreesbyethnicity_degreesbymajorethnicity_enrollbyageattendlevel_enrollbyethn'),
    ]

    operations = [
        migrations.CreateModel(
            name='USNWR',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('rank', models.IntegerField(db_column='RANK')),
                ('name', models.CharField(max_length=500, db_column='NAME')),
            ],
            options={
                'db_table': 'usnwr_rankings',
                'ordering': ['rank'],
                'managed': False,
            },
        ),
    ]
