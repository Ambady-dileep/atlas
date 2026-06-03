from rest_framework import serializers
from .models import Technology, Topic, LearningLog

class TechnologySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Technology
        fields = [
            "id", 
            "name", 
            "description", 
            "created_at", 
            "updated_at",
        ]
        read_only_fields = ["id","created_at", "updated_at",]

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = [
            "id",
            "title",
            "status",
            "technology",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        
class LearningLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LearningLog
        fields = [
            "id",
            "note",
            "duration_minutes",
            "topic",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
 