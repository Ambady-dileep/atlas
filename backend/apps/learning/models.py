from django.db import models
from django.contrib.auth.models import User

class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,related_name="technologies"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.name
    
class Topic(models.Model):
    
    class Status(models.TextChoices):
        NOT_STARTED = "NOT_STARTED", "Not Started"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        COMPLETED = "COMPLETED", "Completed" 
           
    title = models.CharField(max_length=100,null=False,blank=False)
    
    status = models.CharField(
        max_length=20,
        choices = Status.choices,
        default = Status.NOT_STARTED,
    )
    
    technology = models.ForeignKey(
        Technology,
        on_delete=models.CASCADE, related_name="topics"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return self.title
    
class LearningLog(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="learning_logs"
    )
    
    note = models.TextField()

    duration_minutes = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.topic.title} - {self.created_at.date()}"