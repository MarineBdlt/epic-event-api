from rest_framework.viewsets import ModelViewSet
from events.serializers import EventSerializer
from events.models import Event

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

# Create your views here.
