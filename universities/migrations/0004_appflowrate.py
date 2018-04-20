# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0003_usnwr'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppFlowRate',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('app_on', models.DecimalField(decimal_places=10, max_digits=10, db_column='APPONS')),
                ('app_off', models.DecimalField(decimal_places=10, max_digits=10, db_column='APPOFS')),
                ('qual_on', models.DecimalField(decimal_places=10, max_digits=10, db_column='QUALONS')),
                ('qual_off', models.DecimalField(decimal_places=10, max_digits=10, db_column='QUALOFS')),
                ('bqual_on', models.DecimalField(decimal_places=10, max_digits=10, db_column='BQUALONS')),
                ('bqual_off', models.DecimalField(decimal_places=10, max_digits=10, db_column='BQUALOFS')),
                ('hire_on', models.DecimalField(decimal_places=10, max_digits=10, db_column='HIREONS')),
                ('hire_off', models.DecimalField(decimal_places=10, max_digits=10, db_column='HIREOFS')),
            ],
            options={
                'db_table': 'sch_tbl_rates',
                'managed': False,
            },
        ),
    ]
