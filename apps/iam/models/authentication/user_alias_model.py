from apps.iam.enums.UserAliasType import UserAliasType
from apps.iam.models.base_model import BaseModel
from django.db import models
from apps.iam.models.authentication.user_model import UserModel

class UserAliasModel(BaseModel):
    type = models.CharField(max_length=100, choices=UserAliasType.choices)
    value = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_column='user_id')

    class Meta:
        db_table = '"authentication"."user_alias"'
        
