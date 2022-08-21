from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from events.serializers import EventSerializer
from events.models import Event
from events.permissions import IsSupportTeam


class EventViewSet(ModelViewSet):
    permission_classes = [IsAdminUser | IsSupportTeam]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filterset_fields = [
        "client__company_name",
        "client__email",
        "contract__date",
    ]

    def perform_create(self, serializer):
        serializer.save(
            client_id=self.request.data["client_id"],
            contract_id=self.request.data["contract_id"],
        )
