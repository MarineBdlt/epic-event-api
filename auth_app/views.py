from auth_app.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
