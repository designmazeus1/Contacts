from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL



class Contact(models.Model):
    name = models.CharField(max_length = 180)
    phone = models.CharField(max_length = 40)
    updated = models.DateTimeField(auto_now = True, blank = True)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name