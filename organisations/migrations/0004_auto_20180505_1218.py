# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-05-05 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0003_auto_20180505_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='organisations_image'),
        ),
    ]