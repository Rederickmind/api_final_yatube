from rest_framework import permissions, status
from rest_framework.response import Response


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return ((request.method in permissions.SAFE_METHODS)
                or (obj.author == request.user))


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        # return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
