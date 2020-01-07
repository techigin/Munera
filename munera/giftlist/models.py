from django.db import models
from django.conf import settings

# Create your models here.
class Gift(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
            )
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    link = models.CharField(max_length=2083)

    def __str__(self):
        		return self.name

class UserGroup(models.Model):
    admin = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
            )

    group_name = models.CharField(max_length=30)

    def __str__(self):
        		return self.group_name

class GroupMember(models.Model):
    member = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE
            )
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    
