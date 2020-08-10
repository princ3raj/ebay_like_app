# Generated by Django 3.1 on 2020-08-10 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_remove_bid_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('comment_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listings')),
            ],
        ),
    ]