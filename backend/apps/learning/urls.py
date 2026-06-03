from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TechnologyViewSet,TopicViewSet, LearningLogViewSet

router = DefaultRouter()

router.register(r"technologies", TechnologyViewSet, basename="technology")
router.register(r"topics",TopicViewSet, basename="topic")
router.register("logs",LearningLogViewSet,basename="log")

urlpatterns = [
    path("",include(router.urls)),
]
