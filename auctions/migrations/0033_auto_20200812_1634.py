# Generated by Django 3.1 on 2020-08-12 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0032_watchlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bid_price',
            new_name='bidstart',
        ),
    ]
