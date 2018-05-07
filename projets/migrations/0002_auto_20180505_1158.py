# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-05-05 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projet',
            options={'verbose_name_plural': 'projets'},
        ),
        migrations.RemoveField(
            model_name='projet',
            name='titre',
        ),
        migrations.AddField(
            model_name='projet',
            name='image',
            field=models.ImageField(blank=True, upload_to='organisation'),
        ),
        migrations.AddField(
            model_name='projet',
            name='nom',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='projet',
            name='description',
            field=models.TextField(default=''),
        ),
    ]