# Generated by Django 3.1 on 2020-08-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20200810_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='listing_category',
            field=models.CharField(blank=True, choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], max_length=200),
        ),
    ]
