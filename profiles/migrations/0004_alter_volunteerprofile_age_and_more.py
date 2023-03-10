# Generated by Django 4.1.6 on 2023-02-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_skill_skills_skill_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerprofile',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='contact_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='experience',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='preferences',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, choices=[], related_name='skillsInfo', to='profiles.skills'),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
