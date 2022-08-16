from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from clients.serializers import ClientListSerializer, ClientDetailSerializer
from clients.models import Client
from clients.permissions import IsClientReferentInClientView
class ClientViewSet(ModelViewSet):
    permissions_class = (IsAdminUser|IsClientReferentInClientView)
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    queryset = Client.objects.all()
    filterset_fields = ['company_name', 'email']

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
    
