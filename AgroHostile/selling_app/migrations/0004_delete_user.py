# Generated by Django 3.2.7 on 2021-09-25 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selling_app', '0003_fertilizer_location_plant_seller_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
