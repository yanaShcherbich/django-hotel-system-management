# Generated by Django 3.2.2 on 2021-05-09 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20210507_0422'),
        ('booking', '0007_remove_rooms_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rooms',
            new_name='Room',
        ),
    ]
