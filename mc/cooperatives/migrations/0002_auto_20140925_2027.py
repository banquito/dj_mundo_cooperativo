# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperatives', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='contrasena',
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='codigo_postal',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='direccion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='localidad',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='objeto',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
