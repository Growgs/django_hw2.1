# Generated by Django 4.1.7 on 2023-03-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_name_phone_price_phone_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
