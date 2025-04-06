from uuid import UUID

from rest_framework.views import Response
from apps.iam.repositories.authentication import user_repository
from apps.iam.serializers.user_serializer import UserSerializer
from apps.iam.types.user_type import CreateUserInput, RegisterUserInput
from apps.iam.utils.security import SecurityUtils


class UserService:
    user_repository = user_repository.UserRepository()

    def get_user(self, user_id: UUID):
        data = self.user_repository.find_by_id(user_id)

        if data is None:
            return Response(status=404)
        
        serializer = UserSerializer(data)

        return Response(serializer.data, status=200)
    
    def register(self, payload: RegisterUserInput):
        # validate payload here
        existed_user = self.user_repository.find_by_username(payload['username'])

        if existed_user is not None:
            return Response(status=409)
        
        salt = SecurityUtils.generate_salt()

        password = SecurityUtils.hash_password(payload['password'], salt)

        input = CreateUserInput(
            username=payload.get('username'),
            display_name=payload.get('display_name'),
            password=password,
            salt=salt
        )


        user = self.user_repository.create(input)
        
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=201)
