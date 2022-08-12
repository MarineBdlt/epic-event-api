from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from clients.serializers import ClientListSerializer, ClientDetailSerializer
from clients.models import Client
from clients.permissions import IsClientReferentInClientView

class ClientViewSet(ModelViewSet):
    permissions_class = (IsAdminUser|IsClientReferentInClientView)
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()
