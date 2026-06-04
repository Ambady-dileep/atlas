from rest_framework.permissions import BasePermission
from .models import Technology, Topic, LearningLog

class IsOwner(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if isinstance(obj, Technology):
            return obj.user == request.user

        if isinstance(obj, Topic):
            return obj.technology.user == request.user

        if isinstance(obj, LearningLog):
            return obj.topic.technology.user == request.user

        return False