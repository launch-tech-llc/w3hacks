# Generated by Django 2.2.9 on 2020-07-04 03:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200702_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joined_date',
            field=models.DateField(default=datetime.date(2020, 7, 3)),
        ),
    ]
