# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 21:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation_comment',
            name='video',
        ),
        migrations.RemoveField(
            model_name='relation_comment_proj',
            name='proj',
        ),
        migrations.DeleteModel(
            name='Relation_comment',
        ),
        migrations.DeleteModel(
            name='Relation_comment_proj',
        ),
    ]