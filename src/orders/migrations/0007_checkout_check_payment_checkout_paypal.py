# Generated by Django 4.2.11 on 2024-05-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_checkout_order_checkout_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='check_Payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='checkout',
            name='paypal',
            field=models.BooleanField(default=False),
        ),
    ]
