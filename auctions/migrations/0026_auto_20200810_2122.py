# Generated by Django 3.1 on 2020-08-10 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0025_bid_bidder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bidding',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.listings'),
        ),
    ]
