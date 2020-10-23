# Generated by Django 3.1.2 on 2020-10-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinderapp', '0004_customuser_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='position',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
