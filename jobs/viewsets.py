from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .models import Job, Application, Skill
from .serializers import ApplicationSerializer, JobSerializer, SkillSerializer
from common.permissions import ReadOnly

class JobViewSet(ReadOnlyModelViewSet,  mixins.CreateModelMixin, mixins.UpdateModelMixin):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    permission_classes = [IsAuthenticated|ReadOnly]
    filterset_fields = ['company', 'salary', 'title', 'skills']
    ordering_fields = ['title', 'salary', 'company__name']

class SkillViewSet(ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ApplicationViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.user) 