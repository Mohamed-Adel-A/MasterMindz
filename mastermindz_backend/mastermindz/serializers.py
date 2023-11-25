from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group, GroupMember, GroupChat, PrivateChat, GroupTag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupTag
        fields = '__all__'


class GroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = '__all__'

class PrivateChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateChat
        fields = '__all__'