# Generated by Django 4.1.5 on 2023-01-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='User name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('name', models.CharField(max_length=50, verbose_name='Mame')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('image', models.ImageField(blank=True, max_length=200, null=True, upload_to='profile/', verbose_name='Profile image')),
                ('activate_user', models.BooleanField(default=True)),
                ('admin_user', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
