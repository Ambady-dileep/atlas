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
        
class TechnologyNestedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Technology
        fields = [
            "id",
            "name",
        ]
class TopicSerializer(serializers.ModelSerializer):
    
    # Read field
    technology = TechnologyNestedSerializer(read_only=True)
    
    # Write field
    technology_id = serializers.PrimaryKeyRelatedField(
        queryset = Technology.objects.all(),
        source = 'technology',
        write_only = True
    )
    
    def validate_technology(self,technology):
        request = self.context.get("request")
        
        if technology.user != request.user:
            raise serializers.ValidationError(
                "You do not own this technology."
            )
            
        return technology
    class Meta:
        model = Topic
        fields = [
            "id",
            "title",
            "status",
            "technology",
            "technology_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id", 
            "created_at", 
            "updated_at"
        ]
        
class TopicNestedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = [
            "id",
            "title",
            "status",
        ]
class LearningLogSerializer(serializers.ModelSerializer):
    
    # Read field
    topic = TopicNestedSerializer(read_only=True)
    
    # Write field
    topic_id = serializers.PrimaryKeyRelatedField(
        queryset = Topic.objects.all(),
        source = "topic",
        write_only = True,
    )
    
    def validate_topic(self, topic):
        request = self.context.get("request")
        
        if topic.technology.user != request.user:
            raise serializers.ValidationError(
                "You do not own this topic."
            )
            
        return topic
                
    class Meta:
        model = LearningLog
        fields = [
            "id",
            "note",
            "duration_minutes",
            "topic",
            "topic_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
 