# Generated by Django 3.2.3 on 2024-03-06 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='seating_capcity',
            new_name='seating_capacity',
        ),
    ]
