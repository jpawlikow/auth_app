from account_app.views.user_register import CreateUserView
from django.urls import path, include
from rest_framework import routers

from account_app.views.user import UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet, 'user_show')
# router.register('user/register', CreateUserView.as_view(), 'user_register')

urlpatterns = [
    path('user/register/', CreateUserView.as_view(), name='user_register'),
    path('', include(router.urls))
]
