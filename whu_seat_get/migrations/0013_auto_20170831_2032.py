# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whu_seat_get', '0012_auto_20170831_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='is_book',
            field=models.NullBooleanField(default=0),
        ),
    ]
