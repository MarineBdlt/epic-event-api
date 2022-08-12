from rest_framework import permissions
from clients.models import Client
from django.core.exceptions import ObjectDoesNotExist


class IsClientReferentInClientView(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ("destroy", "update", "partial_update"):
            try:
                client = Client.objects.get(id=view.kwargs["pk"])
            except ObjectDoesNotExist:
                return False  
            return request.user == client.sales_contact