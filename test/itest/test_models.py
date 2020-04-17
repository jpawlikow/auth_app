from django.contrib.auth.models import Group
from django.test import TestCase

from account_app.testing.factories import SiteFactory, UserProfileFactory, UserFactory


class TestSiteModel(TestCase):
    def test_site_str_representation(self):
        site = SiteFactory(name='TestSite')
        self.assertEqual(str(site), 'TestSite')


class TestUserProfileModel(TestCase):
    def test_user_profile_str_representation(self):
        user_profile = UserProfileFactory(user=UserFactory(username='TestUser'))
        self.assertEqual(str(user_profile), 'TestUser')


class TestUserModel(TestCase):
    def test_main_group_creating_while_first_user_created(self):
        self.assertEqual(Group.objects.count(), 0)
        UserFactory()
        self.assertEqual(Group.objects.count(), 1)

    def test_main_group_assigning_while_user_created(self):
        user = UserFactory()
        self.assertEqual(user.groups.count(), 1)
        self.assertEqual(user.groups.first().name, 'SIUP Users')
