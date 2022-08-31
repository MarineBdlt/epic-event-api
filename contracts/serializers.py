from contracts.models import Contract
from clients.serializers import ClientListSerializer
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)


class ContractListSerializer(ModelSerializer):
    client_id = SerializerMethodField()

    class Meta:
        model = Contract
        fields = ["id", "title", "status", "client_id"]

    def get_client_id(self, instance):
        query = instance.client
        serializer = ClientListSerializer(query)
        return serializer.data


class ContractDetailSerializer(ModelSerializer):
    client = SerializerMethodField()

    class Meta:
        model = Contract
        fields = "__all__"

    def get_client(self, instance):
        query = instance.client
        serializer = ClientListSerializer(query)
        return serializer.data
