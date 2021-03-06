# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 18:07
from __future__ import unicode_literals

import broadcast.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('live_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=140, unique=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=broadcast.models.get_image_path)),
                ('description', models.TextField(blank=True, null=True)),
                ('stream_key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('public', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ChannelDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=30)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='broadcast.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='ChannelMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='broadcast.Channel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChannelUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='broadcast.Channel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
