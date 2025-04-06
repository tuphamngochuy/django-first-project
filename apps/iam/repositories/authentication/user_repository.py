from apps.iam.models.authentication.user_model import UserModel
from django.core.exceptions import ObjectDoesNotExist

from apps.iam.types.user_type import CreateUserInput


class UserRepository:
    def find_by_username(self, username):
        try:
            return UserModel.objects.get(username=username)
        except ObjectDoesNotExist:
            return None

    
    def find_by_id(self, user_id):
        try:
            return UserModel.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return None
    
    def create(self, payload: CreateUserInput):
        return UserModel.objects.create(**payload)