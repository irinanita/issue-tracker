# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-01 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('bug', 'Bug'), ('feature', 'Feature')], max_length=7)),
                ('label', models.CharField(choices=[('functionality', 'Functionality'), ('design', 'Design')], max_length=13)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
                ('image', models.ImageField(blank='True', null='True', upload_to='img')),
            ],
        ),
    ]
