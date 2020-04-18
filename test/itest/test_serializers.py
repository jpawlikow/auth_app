from account_app.models import Site, UserProfile
from account_app.serializers.user import UserSerializer, SiteSerializer, UserProfileSerializer
from account_app.testing.factories import UserFactory, SiteFactory, UserProfileFactory
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import exceptions


class TestUserSerializer(TestCase):
    def setUp(self):
        self.user_attributes = {
            'username': 'TestUser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@user.com',
            'password': '1234',
        }

        self.user = UserFactory(**self.user_attributes)
        self.serialized_user = UserSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serialized_user.data
        self.assertEqual(data.keys(), {'id', 'username', 'first_name', 'last_name', 'email'})

    def test_id_field_content(self):
        data = self.serialized_user.data
        self.assertEqual(data['id'], 1)

    def test_username_field_content(self):
        data = self.serialized_user.data
        self.assertEqual(data['username'], self.user_attributes['username'])

    def test_first_name_field_content(self):
        data = self.serialized_user.data
        self.assertEqual(data['first_name'], self.user_attributes['first_name'])

    def test_last_name_field_content(self):
        data = self.serialized_user.data
        self.assertEqual(data['last_name'], self.user_attributes['last_name'])

    def test_email_field_content(self):
        data = self.serialized_user.data
        self.assertEqual(data['email'], self.user_attributes['email'])


class TestSiteSerializer(TestCase):

    def setUp(self):
        self.site_attributes = {
            'name': 'TestSite',
        }

        self.site = SiteFactory(**self.site_attributes)
        self.serialized_site = SiteSerializer(instance=self.site)

    def test_contains_expected_fields(self):
        data = self.serialized_site.data
        self.assertEqual(data.keys(), {'id', 'name', })

    def test_id_field_content(self):
        data = self.serialized_site.data
        self.assertEqual(data['id'], 1)

    def test_name_field_content(self):
        data = self.serialized_site.data
        self.assertEqual(data['name'], self.site_attributes['name'])


class TestUserProfileSerializer(TestCase):

    def setUp(self):
        self.site_attributes = {
            'name': 'TestSite',
        }

        self.user_attributes = {
            'username': 'TestUser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@user.com',
            'password': '1234',
        }
        self.user = UserFactory(**self.user_attributes)
        self.serialized_user = UserSerializer(instance=self.user)
        self.site = SiteFactory(**self.site_attributes)
        self.serialized_site = SiteSerializer(instance=self.site)
        self.user_profile = UserProfileFactory(site=self.site, user=self.user)
        self.serialized_user_profile = UserProfileSerializer(instance=self.user_profile)

    def test_contains_expected_fields(self):
        data = self.serialized_user_profile.data
        self.assertEqual(data.keys(), {'id', 'user', 'site'})

    def test_id_field_content(self):
        data = self.serialized_user_profile.data
        self.assertEqual(data['id'], 1)

    def test_site_field_content(self):
        data = self.serialized_user_profile.data
        self.assertEqual(data['site'], self.serialized_site.data)

    def test_user_field_content(self):
        data = self.serialized_user_profile.data
        self.assertEqual(data['user'], self.serialized_user.data)

    def test_create_method(self):
        self.user.delete()
        self.site.delete()

        validated_data = {
            'user': self.user_attributes,
            'site': self.site_attributes,
        }
        user_profile = UserProfileSerializer().create(validated_data)
        self.assertEqual(user_profile.user.id, User.objects.first().id)
        self.assertEqual(user_profile.site.id, Site.objects.first().id)
        self.assertEqual(user_profile.id, UserProfile.objects.first().id)

    def test_create_method_with_inproper_site(self):
        validated_data = {
            'user': self.user_attributes,
            'site': {},
        }
        with self.assertRaises(exceptions.ValidationError):
            UserProfileSerializer().create(validated_data)

    def test_create_method_with_inproper_user(self):
        validated_data = {
            'user': {},
            'site': self.site_attributes,
        }
        with self.assertRaises(exceptions.ValidationError):
            UserProfileSerializer().create(validated_data)
