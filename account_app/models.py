from django.db import models
from django.contrib.auth.models import User, Group
# from rest_framework.authtoken.models import Token


class Site(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    site = models.ForeignKey(Site, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


def assign_groups(sender, instance, created, **kwargs):
    """
    To fill
    """
    if created:
        group_name = 'SIUP Users'
        group, _ = Group.objects.get_or_create(name=group_name)
        instance.groups.add(group)

#
# def assign_token(sender, instance, created, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


models.signals.post_save.connect(assign_groups, sender=User)
# models.signals.post_save.connect(assign_token, sender=User)
