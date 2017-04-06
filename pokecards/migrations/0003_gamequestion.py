# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-06 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokecards', '0002_gamestate'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(default='Example Question?')),
                ('correct_answer', models.TextField(default='Example Correct Answer')),
                ('incorrect_answers', models.TextField(default='PipeDelimited|ListOf|BadAnswers')),
            ],
        ),
    ]
