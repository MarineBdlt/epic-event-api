from rest_framework.serializers import ModelSerializer
from events.models import Event
from rest_framework.serializers import SerializerMethodField
from contracts.serializers import ContractListSerializer
from clients.serializers import ClientListSerializer

class EventSerializer(ModelSerializer):
    contract = SerializerMethodField()
    client = SerializerMethodField()
    class Meta:
        model = Event
        fields = '__all__'
    
    def get_contract(self, instance):
        queryset = instance.contract
        serializer = ContractListSerializer(queryset)
        return serializer.data
    
    def get_client(self, instance):
        queryset = instance.client
        serializer = ClientListSerializer(queryset)
        return serializer.data
