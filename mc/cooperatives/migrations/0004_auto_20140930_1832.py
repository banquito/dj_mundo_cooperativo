# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperatives', '0003_auto_20140929_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_de_asistencia', models.DateTimeField(verbose_name=b'date')),
                ('sede', models.CharField(max_length=200)),
                ('confirmacion', models.NullBooleanField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('partner', models.ForeignKey(to='cooperatives.Partner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cooperative',
            name='descripcion',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
