# Generated by Django 3.0.4 on 2020-04-07 03:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200406_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='id',
            field=models.CharField(default='erbvGJ27', max_length=8, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='joined_date',
            field=models.DateField(default=datetime.date(2020, 4, 7)),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default='9ScZ3Aup', max_length=8, primary_key=True, serialize=False, unique=True),
        ),
    ]
