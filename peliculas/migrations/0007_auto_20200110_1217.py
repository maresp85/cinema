# Generated by Django 3.0.1 on 2020-01-10 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0006_auto_20200110_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 10, 12, 17, 59, 602531)),
        ),
    ]
