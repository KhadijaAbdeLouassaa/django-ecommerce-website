# Generated by Django 4.2.11 on 2024-05-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_decription_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
