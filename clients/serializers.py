from rest_framework.serializers import ModelSerializer
from clients.models import Client
from rest_framework import serializers


class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "company_name", "email"]


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
