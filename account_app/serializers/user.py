from account_app.models import UserProfile, Site
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
            'id': {
                'read_only': True,
            }
        }


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    site = SiteSerializer(required=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'site')
        extra_kwargs = {
            'id': {
                'read_only': True,
            }
        }

    def create(self, validated_data):
        user_serializer = self.fields['user']
        user = user_serializer.create(validated_data['user'])
        site_serializer = self.fields['site']
        site = site_serializer.create(validated_data['site'])
        profile, _ = UserProfile.objects.get_or_create(user=user, site=site)
        return profile
