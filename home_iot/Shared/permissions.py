from rest_framework import permissions
from account.models import User,Profile
from thing.models import Thing
from documentation.models import Documentation


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(permissions.SAFE_METHODS)
        if request.method in permissions.SAFE_METHODS :
            return True
        if hasattr(obj,'email'):
            return obj == request.user
        return obj.owner == request.user
