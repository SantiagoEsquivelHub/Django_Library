# Generated by Django 4.1.5 on 2023-01-16 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='activate_user',
            new_name='active_user',
        ),
    ]
