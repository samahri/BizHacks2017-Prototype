# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-26 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_auto_20170426_0729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageuploadmodel',
            name='description',
        ),
        migrations.AlterField(
            model_name='imageuploadmodel',
            name='model_pic',
            field=models.ImageField(default='none', upload_to='images/'),
        ),
    ]
