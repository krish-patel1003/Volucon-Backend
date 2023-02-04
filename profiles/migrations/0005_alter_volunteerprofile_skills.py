# Generated by Django 4.1.6 on 2023-02-04 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_volunteerprofile_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, choices=[('technical writing', 1), ('logistics', 2), ('PR', 3)], related_name='skillsInfo', to='profiles.skills'),
        ),
    ]