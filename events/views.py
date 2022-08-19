from django.http import request
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from events.serializers import EventSerializer
from events.models import Event
from events.permissions import IsSupportTeam

# ANCHOR IsAdminUser généralisé dans les settings ?
class EventViewSet(ModelViewSet):
    permission_classe = (IsAdminUser|IsSupportTeam)
    serializer_class = EventSerializer
    queryset = Event.objects.all()   
    filterset_fields = ['client__company_name', 'client__email', 'contract__date']
    
    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(
            client_id=self.request.data["client_id"], 
            contract_id=self.request.data["contract_id"]
            )       
        # ANCHOR POURQUOI BESOIN DE CETTE LIGNE ? QUEL RAPPORT AVEC MODELE CLIENT != CLIENT_ID
        # ANCHOR POSTEMAN USERNAME ET PASSWORD EN TROP SUR CONTRACTS

