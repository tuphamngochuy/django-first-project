from django.urls import path

from apps.iam.views.user_view import RegisterUserView, UserDetailView, UserListView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('user/<uuid:user_id>/', UserDetailView.as_view()),
    path('user/register/', RegisterUserView.as_view()),
]
