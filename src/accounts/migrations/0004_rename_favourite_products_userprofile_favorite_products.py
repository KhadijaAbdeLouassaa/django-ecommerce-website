# Generated by Django 4.2.11 on 2024-05-08 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_favourite_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='favourite_products',
            new_name='favorite_products',
        ),
    ]