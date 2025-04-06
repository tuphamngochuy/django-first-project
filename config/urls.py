from django.urls import path, include

urlpatterns = [
    path('api/iam/', include('apps.iam.urls')),
]
