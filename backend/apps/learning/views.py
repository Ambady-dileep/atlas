from rest_framework import viewsets
from .models import Technology, Topic, LearningLog
from .serializers import TechnologySerializer, TopicSerializer, LearningLogSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsOwner

class TechnologyViewSet(viewsets.ModelViewSet):
    serializer_class = TechnologySerializer
    permission_classes = [
        IsAuthenticated,
        IsOwner,
    ]
    
    def get_queryset(self):
        return Technology.objects.filter(user=self.request.user)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    
class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwner,
    ]
    
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    
    filterset_fields = [
        "status",
    ]

    search_fields = [
        "title",
    ]
    
    ordering_fields = [
        "title",
        "created_at",
        "updated_at",
    ]
    
    def get_queryset(self):
        return Topic.objects.select_related(
            "technology"
        ).filter(
            technology__user=self.request.user
        )
    
class LearningLogViewSet(viewsets.ModelViewSet):
    serializer_class = LearningLogSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwner,
    ]
    
    def get_queryset(self):
        return LearningLog.objects.select_related(
            "topic", 
            "topic__technology"
        ).filter(
            topic__technology__user=self.request.user
        )
    