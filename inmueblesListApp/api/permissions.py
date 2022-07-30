from rest_framework import permissions
from inmueblesListApp.models import *

class adminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self,request, view):
        if request.method=="GET":
            return True
        staff_permission=bool(request.user and request.user.is_staff)
        return staff_permission
    
    
class ComentarioUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.Comentarios_user==request.user
        