from django.http import request
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from events.serializers import EventSerializer
from events.models import Event
from events.permissions import IsSupportTeam

# ANCHOR IsAdminUser généralisé dans les settings ?
class EventViewSet(ModelViewSet):
    permission_classes = (IsAdminUser|IsSupportTeam)
    serializer_class = EventSerializer
    queryset = Event.objects.all()

