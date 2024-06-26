# Generated by Django 4.2.11 on 2024-05-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('decription', models.TextField()),
                ('image', models.ImageField(upload_to='blog_images')),
                ('created_at', models.DateField(auto_now=True)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Beauty', 'Beauty'), ('Life Style', 'Life Style'), ('Travel', 'Travel')], max_length=15)),
            ],
        ),
    ]
