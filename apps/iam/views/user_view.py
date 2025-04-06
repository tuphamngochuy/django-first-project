from rest_framework.views import APIView, Response

from apps.iam.serializers.user_serializer import RegisterUserSerializer
from apps.iam.services import user_service

class UserListView(APIView):
    def get(self, request):
	    print(request)


class UserDetailView(APIView):
    user_service = user_service.UserService()
    
    def get(self, _request, user_id):
        return self.user_service.get_user(user_id)

class RegisterUserView(APIView):

    user_service = user_service.UserService()

    def post(self, request):
        serializer: RegisterUserSerializer = RegisterUserSerializer(data=request.data)
        is_valid = serializer.is_valid()
        if not is_valid:
           return Response(serializer.errors, status=400)

        response = self.user_service.register(serializer.typed_data)
        return response
        