from rest_framework import serializers
from apps.iam.models.authentication.user_model import UserModel
from apps.iam.types.user_type import CreateUserInput, RegisterUserInput

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'display_name')

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'display_name', 'password')
    
    @property
    def typed_data(self) -> RegisterUserInput:
        return RegisterUserInput(
            username=self.data['username'],
            display_name=self.data['display_name'],
            password=self.data['password']
        )


    
