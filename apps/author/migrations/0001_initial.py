# Generated by Django 4.1.5 on 2023-01-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=220)),
                ('nacionality', models.CharField(max_length=100)),
                ('state', models.BooleanField(default=True, verbose_name='state')),
                ('creation_date', models.DateField(auto_now=True, verbose_name='Creation date')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('publication_date', models.DateField(verbose_name='Publication date')),
                ('creation_date', models.DateField(auto_now=True, verbose_name='Creation date')),
                ('author_id', models.ManyToManyField(to='author.author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['title'],
            },
        ),
    ]
