from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groups_led')
    category = models.CharField(max_length=255)
    tags = models.ManyToManyField('GroupTag')
    members = models.ManyToManyField(User, through='GroupMember', related_name='groups_joined')
    created_at = models.DateTimeField(auto_now_add=True)


class GroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)


class GroupChat(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class PrivateChat(models.Model):
    participants = models.ManyToManyField(User, related_name='private_chats')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_private_chats')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_private_chats')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class GroupTag(models.Model):
    name = models.CharField(max_length=255)