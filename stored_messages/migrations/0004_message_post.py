# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20150323_1638'),
        ('stored_messages', '0003_auto_20150323_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='post',
            field=models.ForeignKey(related_name='message_post', blank=True, to='posts.Post', null=True),
            preserve_default=True,
        ),
    ]
