from django.db import models
from users.models import User
# Create your models here.
 
class Skills(models.Model):
    skill_name = models.CharField(max_length=255)

    def __str__(self):
        return self.skill_name

class VolunteerProfile(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=20 ,choices=gender_choices, default='M')
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    contact_email = models.EmailField(null=True)
    linkedin = models.URLField(max_length=255, null=True)
    twitter = models.URLField(max_length=255, null=True)
    instagram = models.URLField(max_length=255, null=True)
    skills = models.ManyToManyField(Skills, related_name='skillsInfo', blank=True)
    experience = models.JSONField(null=True)
    preferences = models.JSONField(null=True)







