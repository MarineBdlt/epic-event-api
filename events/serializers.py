from rest_framework.serializers import ModelSerializer
from events.models import Event
from rest_framework.serializers import SerializerMethodField
from contracts.serializers import ContractListSerializer
from clients.serializers import ClientListSerializer
from auth_app.serializers import UserSerializer

class EventSerializer(ModelSerializer):
    contract = SerializerMethodField()
    client = SerializerMethodField()
    # support_team = SerializerMethodField()
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
    
    # def get_support_team(self, instance):
    #     # context={'request': 'request'}
    #     queryset = instance.support_team
    #     print("CONTEXT", self.context)
    #     serializer = UserSerializer(queryset)
 
        return serializer.data
    
    # RECHANGER AVEC UNE FOREIGNKEY
