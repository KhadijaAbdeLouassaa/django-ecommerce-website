# Generated by Django 4.2.11 on 2024-05-16 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='decription',
            new_name='description',
        ),
    ]
