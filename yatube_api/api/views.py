from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post, Follow
from rest_framework import permissions, status, viewsets, filters, mixins
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly, ReadOnly
from .serializers import (
    CommentSerializer, GroupSerializer,
    PostSerializer, FollowSerializer
)
from rest_framework.pagination import LimitOffsetPagination


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthorOrReadOnly
    ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        if serializer.is_valid(self):
            serializer.save(author=self.request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        ReadOnly
    ]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsAuthorOrReadOnly
    ]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        comment_id = self.kwargs.get('comment_id')
        if comment_id:
            return Comment.objects.filter(id=comment_id, post=post)
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        if serializer.is_valid(self):
            serializer.save(author=self.request.user, post=post)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
