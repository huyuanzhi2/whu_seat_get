# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whu_seat_get', '0013_auto_20170831_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='starttime',
            field=models.DateTimeField(null=True),
        ),
    ]
