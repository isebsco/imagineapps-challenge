from rest_framework import serializers
from apiConsumerApp.models import CocoaContract


class CocoaContractSerializer(serializers.ModelSerializer):
    """
    A simple serializer for our CocoaContracts model
    """
    id = serializers.ReadOnlyField()  
    data = serializers.JSONField()

    class Meta:
        model = CocoaContract
        fields = ('id', 'data')
