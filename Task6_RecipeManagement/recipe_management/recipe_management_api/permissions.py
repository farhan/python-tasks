from rest_framework import permissions


class CreateOwnRecipe(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to create/update their own recipe."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.created_by.id == request.user.id
