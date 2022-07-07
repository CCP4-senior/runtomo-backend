from rest_framework import permissions

class IsCommentUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.comment_user == request.user or request.user.is_staff