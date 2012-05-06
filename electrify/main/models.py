from django.db import models
from django.contrib.auth.models import User

class AccountNumber(models.Model):
  account_number = models.CharField(max_length=128)

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  zip_code = models.CharField(max_length=12)
  account_numbers = models.ManyToManyField(AccountNumber, related_name="members")
