# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap_blog', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(
                2015, 2, 3, 1, 45, 44, 649809,
                 tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(
                2015, 2, 3, 1, 45, 54, 265760,
                 tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(
                2015, 2, 3, 1, 46, 7, 209558,
                 tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
