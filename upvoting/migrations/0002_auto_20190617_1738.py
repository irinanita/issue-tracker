# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-17 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upvoting', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userticketvote',
            old_name='ticket',
            new_name='ticketID',
        ),
    ]
