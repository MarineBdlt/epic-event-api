from clients.serializers import ClientListSerializer
from clients.models import Client
from rest_framework.viewsets import ModelViewSet

class ClientViewSet(ModelViewSet):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()
