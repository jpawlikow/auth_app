from account_app.models import Site, UserProfile
from django.contrib.auth.models import User, Group
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username', )

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.SelfAttribute('first_name')
    password = factory.PostGenerationMethodCall('set_password', 'password')


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group
        django_get_or_create = ('name', )

    name = factory.Faker('name')


class SiteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Site
        django_get_or_create = ('name', )

    name = factory.Faker('name')


class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)
    site = factory.SubFactory(SiteFactory)
