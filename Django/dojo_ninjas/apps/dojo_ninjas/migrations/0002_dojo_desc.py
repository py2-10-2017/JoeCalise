# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='A Coding Dojo facility'),
            preserve_default=False,
        ),
    ]