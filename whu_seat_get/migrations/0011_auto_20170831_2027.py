# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whu_seat_get', '0010_auto_20170831_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='is_book',
            field=models.CharField(blank=True, default=0, max_length=1),
        ),
    ]
