# Generated by Django 3.1.7 on 2021-04-02 04:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapplication', '0006_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='location',
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='location name', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
