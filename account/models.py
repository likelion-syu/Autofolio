from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
	email = models.CharField(max_length=30, blank=False)