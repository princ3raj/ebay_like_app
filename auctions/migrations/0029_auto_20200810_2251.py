# Generated by Django 3.1 on 2020-08-10 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_auto_20200810_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='listing_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]