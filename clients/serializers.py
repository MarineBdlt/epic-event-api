from rest_framework.serializers import ModelSerializer
from clients.models import Client


class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "company_name",
            "email",
            "sales_contact",
        ]


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
