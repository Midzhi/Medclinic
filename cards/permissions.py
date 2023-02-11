from rest_framework.permissions import BasePermission


class IsOwnerOrCreate(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.method == 'POST':
            return True
        return request.user == obj.user or request.user.is_superuser
