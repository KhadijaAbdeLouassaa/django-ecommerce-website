# Generated by Django 4.2.11 on 2024-07-24 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=15, verbose_name='full_name')),
                ('phone_number', models.CharField(max_length=15, verbose_name='phone_number')),
                ('city', models.CharField(max_length=20, verbose_name='city')),
                ('address1', models.CharField(max_length=50, verbose_name='address1')),
                ('address2', models.CharField(blank=True, max_length=50, null=True, verbose_name='address2')),
                ('zip', models.CharField(max_length=15, verbose_name='zip')),
                ('order_note', models.TextField(blank=True, null=True, verbose_name='order_note')),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
