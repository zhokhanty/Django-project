from rest_framework.permissions import BasePermission, SAFE_METHODS

def check_role(user, role):
    profile = getattr(user, 'profile', None)
    return profile and profile.role == role

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        if request.user and check_role(request.user, 'admin'):
            return True

        print("User on administrator:", request.user)
        return False