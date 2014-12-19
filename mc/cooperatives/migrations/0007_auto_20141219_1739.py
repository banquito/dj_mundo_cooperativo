# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperatives', '0006_auto_20140930_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assembly',
            name='notificacion',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='partner',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date published'),
        ),
    ]
