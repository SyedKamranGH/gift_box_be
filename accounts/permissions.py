from rest_framework import permissions

class IsBuyer(permissions.BasePermission):
    """
    Custom permission to only allow buyers to access certain views.
    """
    def has_permission(self, request, view):
        def has_permission(self, request, view):
            return request.user.is_authenticated and request.user.role == 'buyer'
        
class IsSeller(permissions.BasePermission):
    """
    Custom permission to only allow sellers to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'seller'
    
    
class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admins to access certain views.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'