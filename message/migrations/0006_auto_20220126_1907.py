# Generated by Django 3.0 on 2022-01-26 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20220126_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 19, 7, 11, 338940)),
        ),
    ]
