# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 20:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(default=datetime.datetime(2017, 7, 23, 20, 41, 9, 639853, tzinfo=utc))),
                ('consists_of', models.CharField(max_length=100)),
                ('priced', models.IntegerField()),
                ('status', models.CharField(choices=[('D', 'declined_order'), ('A', 'accepted_order'), ('F', 'finished_order')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(choices=[('M', 'moscow'), ('S-P', 'sankt-peterburg')], max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='rest_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zakaz.Restaurant'),
        ),
    ]
