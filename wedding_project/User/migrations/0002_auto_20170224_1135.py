# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 11:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wedding',
            name='bride',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='groom',
        ),
        migrations.RemoveField(
            model_name='present',
            name='wedding_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='present',
            name='reserved_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Wedding',
        ),
    ]
