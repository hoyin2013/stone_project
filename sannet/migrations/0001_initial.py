# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('deviceImage', models.ImageField(upload_to=b'', null=True, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('deviceModel', models.CharField(max_length=50, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe5\x9e\x8b\xe5\x8f\xb7')),
                ('comp', models.CharField(max_length=50, verbose_name=b'\xe7\x94\x9f\xe4\xba\xa7\xe5\x8e\x82\xe5\xae\xb6')),
                ('compTel', models.CharField(max_length=20, null=True, verbose_name=b'\xe5\xae\xa2\xe6\x9c\x8d\xe7\x94\xb5\xe8\xaf\x9d', blank=True)),
                ('price', models.PositiveSmallIntegerField(null=True, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc', blank=True)),
                ('parameter', models.TextField(null=True, verbose_name=b'\xe6\x80\xa7\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('remark', models.TextField(null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
            ],
            options={
                'verbose_name': '\u8bbe\u5907',
                'verbose_name_plural': '\u8bbe\u5907',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
            options={
                'verbose_name': '\u8bbe\u5907\u7c7b\u578b',
                'verbose_name_plural': '\u8bbe\u5907\u7c7b\u578b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pname', models.CharField(unique=True, max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
                ('position', models.CharField(max_length=100, verbose_name=b'\xe6\x96\xbd\xe5\xb7\xa5\xe5\x9c\xb0\xe7\x82\xb9')),
                ('comp', models.CharField(max_length=100, verbose_name=b'\xe6\x96\xbd\xe5\xb7\xa5\xe5\x8d\x95\xe4\xbd\x8d')),
                ('startTime', models.DateField(null=True, verbose_name=b'\xe5\x90\xaf\xe5\x8a\xa8\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('finishedTime', models.DateField(null=True, verbose_name=b'\xe7\xab\xa3\xe5\xb7\xa5\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('config', models.FileField(upload_to=b'uploads', null=True, verbose_name=b'\xe9\x85\x8d\xe7\xbd\xae\xe6\x96\x87\xe4\xbb\xb6', blank=True)),
                ('desc', models.TextField(null=True, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0\xe4\xbf\xa1\xe6\x81\xaf', blank=True)),
            ],
            options={
                'verbose_name': '\u9879\u76ee',
                'verbose_name_plural': '\u9879\u76ee',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deviceNum', models.PositiveSmallIntegerField(verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe6\x95\xb0\xe9\x87\x8f')),
                ('device', models.ForeignKey(verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe5\x90\x8d\xe7\xa7\xb0', to='sannet.Device')),
                ('project', models.ForeignKey(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae', to='sannet.Project')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u8bbe\u5907',
                'verbose_name_plural': '\u9879\u76ee\u8bbe\u5907',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe5\x90\x8d\xe7\xa7\xb0')),
                ('comment', models.TextField(verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe8\xaf\xb4\xe6\x98\x8e')),
            ],
            options={
                'verbose_name': '\u8bbe\u5907\u7c7b\u522b',
                'verbose_name_plural': '\u8bbe\u5907\u7c7b\u522b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='belongSystem',
            field=models.ForeignKey(verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab', to='sannet.System'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='deviceType',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\xb1\xbb\xe5\x9e\x8b', to='sannet.DeviceType'),
            preserve_default=True,
        ),
    ]
