from account_app.models import UserProfile
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from account_app.serializers.user import UserProfileSerializer


class CreateUserView(CreateAPIView):

    model = UserProfile
    permission_classes = [permissions.AllowAny, ]
    serializer_class = UserProfileSerializer


