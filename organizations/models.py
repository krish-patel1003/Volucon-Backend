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



