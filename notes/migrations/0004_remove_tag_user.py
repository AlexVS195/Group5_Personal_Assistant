# Generated by Django 5.0.3 on 2024-05-03 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
    ]
