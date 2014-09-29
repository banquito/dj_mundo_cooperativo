# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperatives', '0002_auto_20140925_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperative',
            name='codigo_postal',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='direccion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='localidad',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='objeto',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='correo_electronico',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='fax',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
