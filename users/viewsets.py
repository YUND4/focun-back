from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from .serializers import UserSerializerSerializer
from .models import User
from drf_yasg.utils import swagger_auto_schema

class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.none()
    serializer_class = UserSerializerSerializer

    @swagger_auto_schema(request_body=UserSerializerSerializer)
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "message": "User created successfully",
                "user": UserSerializerSerializer(user).data
            },
            status=status.HTTP_201_CREATED
        )

