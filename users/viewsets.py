from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User
from drf_yasg.utils import swagger_auto_schema

class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.none()
    serializer_class = UserSerializer
    permission_classes = ()

    @swagger_auto_schema(request_body=UserSerializer)
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "message": "User created successfully",
                "user": UserSerializer(user).data
            },
            status=status.HTTP_201_CREATED
        )
class UserMeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.none()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        return Response(
            UserSerializer(request.user.user).data
        )

