# Generated by Django 3.0.4 on 2020-04-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200406_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='id',
            field=models.CharField(default='zgZ3kRr3', max_length=8, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(default='280YFwNg', max_length=8, primary_key=True, serialize=False, unique=True),
        ),
    ]