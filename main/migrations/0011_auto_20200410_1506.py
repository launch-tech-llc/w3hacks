# Generated by Django 3.0.4 on 2020-04-10 22:06

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200410_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='id',
            field=models.CharField(default=main.models.generate_id, max_length=8, primary_key=True, serialize=False, unique=True),
        ),
    ]
