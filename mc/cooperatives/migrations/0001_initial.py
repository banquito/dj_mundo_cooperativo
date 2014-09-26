# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('objeto', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('localidad', models.CharField(max_length=200)),
                ('codigo_postal', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('siglas', models.CharField(max_length=200)),
                ('domicilio', models.CharField(max_length=200)),
                ('codigo_postal', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('provincia', models.CharField(max_length=200)),
                ('prefijo', models.IntegerField()),
                ('telefonos', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200, null=True)),
                ('correo_electronico', models.CharField(max_length=200, null=True)),
                ('director', models.CharField(max_length=200)),
                ('director2', models.CharField(max_length=200, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('correo_electronico', models.CharField(max_length=200)),
                ('contrasena', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('localidad', models.CharField(max_length=200)),
                ('dni', models.IntegerField(default=0)),
                ('fecha_de_nacimiento', models.DateTimeField(verbose_name=b'date')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('cooperative', models.ForeignKey(to='cooperatives.Cooperative')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cooperative',
            name='provincia',
            field=models.ForeignKey(to='cooperatives.Organization'),
            preserve_default=True,
        ),
    ]
