from django.db import models
from apps.iam.models.base_model import BaseModel

class UserModel(BaseModel):
    display_name = models.CharField(max_length=100, null=False, blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    salt = models.CharField(max_length=100, null=True, blank=True)
    last_login_at = models.DateTimeField(null=True, blank=True)
    is_anonymous = models.BooleanField(default=True) #type: ignore

    class Meta:
        db_table = '"authentication"."user"'
