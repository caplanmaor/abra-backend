# Generated by Django 4.0.4 on 2022-05-28 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_rename_title_message_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Body',
            new_name='body',
        ),
    ]
