# Generated by Django 4.0.2 on 2023-11-20 19:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 11, 20, 19, 29, 31, 450906)),
        ),
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.guild'),
        ),
    ]