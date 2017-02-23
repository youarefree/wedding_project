# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present_name', models.CharField(blank=True, max_length=128, null=True)),
                ('approved', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(default='password', max_length=128)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bride', to='User.User')),
                ('groom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groom', to='User.User')),
            ],
        ),
        migrations.AddField(
            model_name='present',
            name='reserved_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User'),
        ),
        migrations.AddField(
            model_name='present',
            name='wedding_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Wedding'),
        ),
        migrations.AddField(
            model_name='comment',
            name='present_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Present'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User'),
        ),
    ]