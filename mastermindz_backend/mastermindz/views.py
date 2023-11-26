from rest_framework import generics
from django.contrib.auth.models import User
from .models import Group, GroupMember, GroupChat, PrivateChat, GroupTag
from .serializers import UserSerializer, GroupSerializer, GroupMemberSerializer
from .serializers import GroupTagSerializer, GroupChatSerializer, PrivateChatSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupListView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupMembersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return User.objects.filter(groups_joined__id=group_id)

class GroupTagListView(generics.ListCreateAPIView):
    queryset = GroupTag.objects.all()
    serializer_class = GroupTagSerializer

class GroupTagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupTag.objects.all()
    serializer_class = GroupTagSerializer

class GroupChatListView(generics.ListCreateAPIView):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer

class PrivateChatListView(generics.ListCreateAPIView):
    queryset = PrivateChat.objects.all()
    serializer_class = PrivateChatSerializer