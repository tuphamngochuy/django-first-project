from django.db import models
from django.db.models.fields import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=False) #type: ignore
    
    objects = models.Manager()
    class Meta:
        abstract = True