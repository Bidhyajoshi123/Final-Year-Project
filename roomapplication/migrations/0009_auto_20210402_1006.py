# Generated by Django 3.1.7 on 2021-04-02 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapplication', '0008_auto_20210402_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
