# Generated by Django 3.2.4 on 2021-06-24 21:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foo',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 24, 21, 54, 11, 115696, tzinfo=utc)),
        ),
    ]
