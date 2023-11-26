from django.urls import path
from .views import (
    UserListView, UserDetailView, GroupListView, GroupDetailView,
    GroupTagListView, GroupTagDetailView, GroupChatListView, PrivateChatListView,
    GroupMembersView,
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('groups/', GroupListView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('group-tags/', GroupTagListView.as_view(), name='group-tag-list'),
    path('group-tags/<int:pk>/', GroupTagDetailView.as_view(), name='group-tag-detail'),
    path('group-chats/', GroupChatListView.as_view(), name='group-chat-list'),
    path('private-chats/', PrivateChatListView.as_view(), name='private-chat-list'),
    path('groups/<int:group_id>/members/', GroupMembersView.as_view(), name='group-members'),
]