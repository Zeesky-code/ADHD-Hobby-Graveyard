# Generated by Django 3.2.8 on 2021-10-11 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0002_alter_hobby_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hobby',
            old_name='stillInterested',
            new_name='Faded',
        ),
    ]
