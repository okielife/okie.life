# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-10 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_auto_20170410_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(null=True),
        ),
    ]
