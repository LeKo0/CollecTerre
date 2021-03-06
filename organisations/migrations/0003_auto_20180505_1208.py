# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-05-05 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0002_auto_20180505_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='organisation_image'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='phone',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='website',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
