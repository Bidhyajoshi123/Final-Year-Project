# Generated by Django 3.1.7 on 2021-03-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapplication', '0003_auto_20210322_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
