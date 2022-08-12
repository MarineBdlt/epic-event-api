from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from events.models import Event

# ANCHOR filtres dans la vue ou permissions ?

class IsSupportTeam(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ("destroy", "update", "partial_update"):
            try:
                event = Event.objects.get(id=view.kwargs["pk"])
            except ObjectDoesNotExist:
                return False            
            return request.user in event.support_team.all()