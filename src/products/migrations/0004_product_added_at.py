# Generated by Django 4.2.11 on 2024-04-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_at',
            field=models.DateField(auto_now=True),
        ),
    ]
