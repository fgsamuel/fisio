# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_auto_20150610_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliador',
            name='login',
        ),
        migrations.RemoveField(
            model_name='avaliador',
            name='senha',
        ),
    ]