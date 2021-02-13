from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255, editable=False, unique=True)
    hashed_key = models.CharField(max_length=255, editable=False, unique=True)


