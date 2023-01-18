# Generated by Django 4.1.5 on 2023-01-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, max_length=225, null=True, upload_to='books/', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='book',
            name='stock',
            field=models.SmallIntegerField(default=1, verbose_name='Stock'),
        ),
    ]