# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_text', models.CharField(max_length=200)),
            ],
        ),
    ]
