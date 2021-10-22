from django.shortcuts import get_object_or_404

from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)
from posts.models import Comment, Follow, Group, Post


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    # пермишен AuthorOrReadOnly стоит по умолчанию в settings
    # он и будет использоваться в этом вьюсете


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # используется пермишен по умолчанию

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        get_object_or_404(Post, pk=post_id)
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter)
    search_fields = ('following__username',)

    def get_queryset(self):
        user_id = self.request.user
        get_object_or_404(Follow, pk=user_id)
        new_queryset = Follow.objects.filter(user=user_id)
        return new_queryset
