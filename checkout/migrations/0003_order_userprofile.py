# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-08 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_location'),
        ('checkout', '0002_auto_20201008_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='userprofile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='accounts.Profile'),
        ),
    ]
