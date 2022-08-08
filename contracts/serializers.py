from contracts.models import Contract
from clients.serializers import ClientListSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField

class ContractListSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "title", "status"]

class ContractDetailSerializer(ModelSerializer):  
    client = SerializerMethodField() 
    class Meta:
        model = Contract
        fields = '__all__'
    
    def get_client(self, instance):
        queryset = instance.client
        serializer = ClientListSerializer(queryset)
        return serializer.data
        