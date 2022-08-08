from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from contracts.serializers import ContractDetailSerializer
from contracts.models import Contract
from events.models import Event

class ContractViewSet(ModelViewSet):
    serializer_class = ContractDetailSerializer
    queryset = Contract.objects.all()
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
        
    def perform_update(self, serializer):
        serializer.save()
        data = self.request.data
        if data["status"] == "SIGNE":
            print("HERE")
            contract = get_object_or_404(Contract, id=self.kwargs.get("pk"))
            new_event = Event(contract=contract, client=contract.client)
            new_event.save()
        serializer.save()
