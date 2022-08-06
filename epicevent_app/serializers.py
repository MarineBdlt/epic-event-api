from django.contrib.auth.models import User
from epicevent_app.models import Client
import rest_framework 
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ContractSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
# class ContractStatusSerializer(ModelSerializer):
#     class Meta:
#         model = Client
#         fields = '__all__'
        
class EventSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'