# Generated by Django 4.1.7 on 2023-03-04 22:56

import app.data
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='image',
            field=models.FileField(blank=True, upload_to=app.data.upload_path),
        ),
    ]