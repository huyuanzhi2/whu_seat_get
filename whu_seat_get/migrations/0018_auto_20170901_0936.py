# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whu_seat_get', '0017_auto_20170901_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='build',
            field=models.CharField(choices=[(1, 'asda'), (2, 'n'), (3, 'wwe')], max_length=50, null=True),
        ),
    ]