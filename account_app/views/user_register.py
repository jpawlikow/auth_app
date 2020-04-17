from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from account_app.serializers.user import UserProfileSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserProfileSerializer


