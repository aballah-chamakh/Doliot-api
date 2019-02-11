from rest_framework import permissions
from account.models import User,Profile
from thing.models import Bulb
from documentation.models import Documentation


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS :
            return True
        if hasattr(obj,'email'):
            return obj == request.user
        print('this is a thing model')
        print(request.user.username)
        print(obj.owner)
        return obj.owner == request.user
