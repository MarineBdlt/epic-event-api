from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from epicevent_app.models import Client, Contract, Event
from epicevent_app.serializers import UserSerializer, ClientSerializer, ContractSerializer, EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    
class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
# class ContractStatusViewSet(ModelViewSet):
#     serializer_class = ContractSerializer
#     queryset = ContractStatus.objects.all()

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    # permission_classes

    # serializer_class = serializers.CommentDetailSerializer
    # post_serializer_class = serializers.CommentListSerializer

    # def get_serializer_class(self):
    #     if self.action in ("create", "update"):
    #         return self.post_serializer_class
    #     return super().get_serializer_class()

    # def perform_create(self, serializer):
    #     issue = get_object_or_404(Issue, pk=self.kwargs["issue_pk"])
    #     serializer.save(
    #         author_user_id=self.request.user,
    #         issue_id=issue,
    #     )

# Create your views here.
