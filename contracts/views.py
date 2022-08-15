from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from contracts.serializers import ContractDetailSerializer
from contracts.models import Contract
from contracts.permissions import IsClientReferentInContractView
from events.models import Event
from django_filters.rest_framework import DjangoFilterBackend

class ContractViewSet(ModelViewSet):
    serializer_class = ContractDetailSerializer
    queryset = Contract.objects.all()
    permission_class = (IsAdminUser|IsClientReferentInContractView)   
        
    def perform_update(self, serializer):
        print(self.request.data)
        serializer.save()
        data = self.request.data
        if data["status"] == "SIGNE":
            contract = get_object_or_404(Contract, id=self.kwargs.get("pk"))
            new_event = Event(contract=contract, client=contract.client)
            new_event.save()
        serializer.save()
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client__company_name', 'client__email', 'date', 'amount']
