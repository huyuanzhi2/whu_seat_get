# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whu_seat_get', '0003_auto_20170831_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='is_book',
            field=models.BooleanField(default=None),
        ),
    ]
