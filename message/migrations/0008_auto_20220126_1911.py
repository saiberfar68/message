# Generated by Django 3.0 on 2022-01-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0007_auto_20220126_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
