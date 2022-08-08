from rest_framework.viewsets import ModelViewSet
from contracts.serializers import ContractSerializer
from contracts.models import Contract

class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()