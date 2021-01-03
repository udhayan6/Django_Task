from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmed = models.BooleanField("Confirmed", default=False)

    city = models.CharField("City", max_length=50, blank=True)
    state = models.CharField("State", max_length=50, blank=True)
    country = models.CharField("Country", max_length=50, blank=True)
    referral = models.CharField("Referral", max_length=50, blank=True)

def __str__(self):
    return f'{self.user.username} Profile'

def save(self, *args, **kwargs):
    super().save(*args, **kwargs)