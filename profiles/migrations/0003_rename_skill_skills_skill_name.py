# Generated by Django 4.1.6 on 2023-02-04 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_volunteerprofile_remove_personalinfo_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='skill',
            new_name='skill_name',
        ),
    ]
