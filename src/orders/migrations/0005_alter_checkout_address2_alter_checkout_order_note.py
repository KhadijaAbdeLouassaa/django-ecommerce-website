# Generated by Django 4.2.11 on 2024-05-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_checkout_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='address2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='order_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
