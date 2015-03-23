# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stored_messages', '0002_auto_20150323_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='in_response_to',
            new_name='thread',
        ),
    ]
