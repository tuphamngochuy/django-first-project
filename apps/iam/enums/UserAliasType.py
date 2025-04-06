from django.db import models

class UserAliasType(models.TextChoices):
    EMAIL = 'email'
    PHONE = 'phone'
    