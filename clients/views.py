from clients.serializers import ClientSerializer
from clients.models import Client
from rest_framework.viewsets import ModelViewSet

class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
