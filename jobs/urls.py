from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ApplicationViewSet, JobViewSet, SkillViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'skills', SkillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]