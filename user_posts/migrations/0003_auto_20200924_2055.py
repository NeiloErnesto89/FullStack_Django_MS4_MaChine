# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-24 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_posts', '0002_auto_20200720_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_posts',
            name='title',
            field=models.CharField(help_text='Enter post title', max_length=100),
        ),
    ]