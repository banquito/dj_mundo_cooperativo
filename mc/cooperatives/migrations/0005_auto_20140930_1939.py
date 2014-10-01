# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cooperatives', '0004_auto_20140930_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_de_convocatoria', models.DateTimeField(verbose_name=b'date')),
                ('notificacion', models.BooleanField()),
                ('direccion', models.CharField(max_length=200)),
                ('localidad', models.CharField(max_length=200)),
                ('codigo_postal', models.CharField(max_length=200)),
                ('fecha_inicio_asamblea', models.DateTimeField(verbose_name=b'date')),
                ('fecha_fin_asamblea', models.DateTimeField(verbose_name=b'date')),
                ('fecha_inicio_consejo', models.DateTimeField(verbose_name=b'date')),
                ('fecha_fin_consejo', models.DateTimeField(verbose_name=b'date')),
                ('cooperative', models.ForeignKey(to='cooperatives.Cooperative')),
                ('miembros_consejo_1', models.OneToOneField(related_name=b'consejo_1', to='cooperatives.Partner')),
                ('miembros_consejo_2', models.OneToOneField(related_name=b'consejo_2', to='cooperatives.Partner')),
                ('miembros_consejo_3', models.OneToOneField(related_name=b'consejo_3', to='cooperatives.Partner')),
                ('miembros_consejo_presidente', models.OneToOneField(related_name=b'consejo_presidente', to='cooperatives.Partner')),
                ('miembros_consejo_secretario', models.OneToOneField(related_name=b'consejo_secretario', to='cooperatives.Partner')),
                ('miembros_consejo_tesorero', models.OneToOneField(related_name=b'consejo_tesorero', to='cooperatives.Partner')),
                ('precide_asamblea', models.OneToOneField(related_name=b'precide', to='cooperatives.Partner')),
                ('sindico_suplente', models.OneToOneField(related_name=b'suplente', to='cooperatives.Partner')),
                ('sindico_titular', models.OneToOneField(related_name=b'sindico', to='cooperatives.Partner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cooperative',
            name='capital_banco',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='capital_direccion',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='capital_fecha',
            field=models.DateTimeField(null=True, verbose_name=b'date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='capital_monto',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='capital_numero',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='cuit',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='expediente',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='matricula',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='presentacion',
            field=models.DateTimeField(null=True, verbose_name=b'date', blank=True),
            preserve_default=True,
        ),
    ]
