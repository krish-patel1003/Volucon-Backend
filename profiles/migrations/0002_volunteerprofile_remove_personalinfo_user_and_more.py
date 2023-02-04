# Generated by Django 4.1.6 on 2023-02-04 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=20)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('linkedin', models.URLField(max_length=255, null=True)),
                ('twitter', models.URLField(max_length=255, null=True)),
                ('instagram', models.URLField(max_length=255, null=True)),
                ('experience', models.JSONField()),
                ('preferences', models.JSONField()),
                ('skills', models.ManyToManyField(blank=True, related_name='skillsInfo', to='profiles.skills')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='skillsinfo',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='skillsinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='socialinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='ExperienceInfo',
        ),
        migrations.DeleteModel(
            name='PersonalInfo',
        ),
        migrations.DeleteModel(
            name='SkillsInfo',
        ),
        migrations.DeleteModel(
            name='SocialInfo',
        ),
    ]