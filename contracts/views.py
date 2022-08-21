from webbrowser import get
from django.db import IntegrityError
from django.forms import ValidationError
from django.http import request, response
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from contracts.models import Contract
from contracts.permissions import IsClientReferentInContractView
from contracts.serializers import ContractDetailSerializer, ContractListSerializer
from events.models import Event
from clients.models import Client
from rest_framework.response import Response
from rest_framework import status


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    permission_class = IsAdminUser | IsClientReferentInContractView
    filterset_fields = ["client__company_name", "client__email", "date", "amount"]

    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_update(self, serializer):
        serializer.save()
        data = self.request.data
        if data and data["status"] and data["status"] == "S":
            contract = get_object_or_404(Contract, id=self.kwargs.get("pk"))
            new_event = Event(contract=contract, client=contract.client)
            new_event.save()
        serializer.save()

    def perform_create(self, serializer):
        serializer.save(client_id=self.request.data["client_id"])
        serializer.save()
