from django.db import models
from users.models import User
# Create your models here.
class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=255, null=True)
    profile_pic = models.ImageField(upload_to='org_profile_pics/', null=True, blank=True)
    description = models.TextField(null=True)
    website = models.URLField(null=True)
    code_of_conduct = models.URLField(null=True)
    domain = models.JSONField(null=True)

    def __str__(self):
        return self.org_name


class Event(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    location = models.TextField(null=True)
    website = models.URLField(null=True)
    code_of_conduct = models.URLField(null=True)
    requirement = models.JSONField(null=True)

    def __str__(self):
        return f'{self.organization} - {self.event_name}'







