# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20170224_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='present',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]