from django.test import Client
from contracts.models import Contract
from clients.serializers import ClientListSerializer
from auth_app.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField
from clients.models import Client

class ContractListSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "title", "status", "client_id"]

class ContractDetailSerializer(ModelSerializer):  
    client = SerializerMethodField() 
    class Meta:
        model = Contract
        fields = '__all__'
    
    def get_client(self, instance):
        query = instance.client
        serializer = ClientListSerializer(query)
        return serializer.data