# Generated by Django 3.2.1 on 2022-01-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timepad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
