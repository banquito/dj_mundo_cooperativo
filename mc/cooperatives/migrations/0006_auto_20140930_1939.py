# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperatives', '0005_auto_20140930_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assembly',
            name='notificacion',
            field=models.BooleanField(verbose_name=1),
        ),
    ]
