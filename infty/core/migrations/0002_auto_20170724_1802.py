# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-24 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='type',
            field=models.PositiveSmallIntegerField(default=5, verbose_name=[(0, 'Need'), (1, 'Goal'), (2, 'Idea'), (3, 'Plan'), (4, 'Step'), (5, 'Task')]),
        ),
    ]
