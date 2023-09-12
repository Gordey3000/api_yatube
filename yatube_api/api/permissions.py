from rest_framework import permissions


class VerificationOfAutorPermission(permissions.BasePermission):
    message = 'Изменение и удаление чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
