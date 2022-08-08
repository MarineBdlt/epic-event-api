from contracts.models import Contract
from rest_framework.serializers import ModelSerializer

class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'