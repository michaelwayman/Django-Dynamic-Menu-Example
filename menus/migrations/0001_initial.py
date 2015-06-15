# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show_in_menu', models.BooleanField(default=False)),
                ('live', models.BooleanField(default=False)),
                ('url', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=32)),
            ],
        ),
    ]
