# Generated by Django 4.1.6 on 2023-02-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_volunteerprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='volu_profile_pics/'),
        ),
    ]
