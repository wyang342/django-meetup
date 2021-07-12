from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    groups = models.ManyToManyField('Group', related_name='users')


class Group(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='owned_groups')
    desc = models.TextField()

    def __str__(self):
        return self.title


class Event(models.Model):
    group = models.ForeignKey(
        'Group', on_delete=models.CASCADE, related_name='events')
    date = models.DateField()
    title = models.CharField(max_length=255)
    desc = models.TextField()
    image_path = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.title
