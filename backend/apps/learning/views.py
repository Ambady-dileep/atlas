from rest_framework import viewsets
from .models import Technology, Topic, LearningLog
from .serializers import TechnologySerializer, TopicSerializer, LearningLogSerializer
from rest_framework.permissions import IsAuthenticated

class TechnologyViewSet(viewsets.ModelViewSet):
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Technology.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    
class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Topic.objects.filter(technology__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save()
    
class LearningLogViewSet(viewsets.ModelViewSet):
    serializer_class = LearningLogSerializer
    permission_classes = [IsAuthenticated]
    
    def get_query(self):
        return LearningLog.objects.filter(topic__technology__user = self.request.user)