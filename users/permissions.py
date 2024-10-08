from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)
    
    
class IsMakerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_maker)
        
class IsCustomerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_customer)
     
     
