from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from contracts.models import Contract


class IsClientReferentInContractView(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ("destroy", "update", "partial_update"):
            try:
                contract = Contract.objects.get(id=view.kwargs["pk"])
            except ObjectDoesNotExist:
                return False
            return request.user == contract.client.sales_contact
        else:
            return True
