from rest_framework import serializers
from apiConsumerApp.models import CocoaContracts


class CustomerDataSerializer(serializers.ModelSerializer):
    """
    A simple serializer for our CocoaContracts model
    """
    id = serializers.ReadOnlyField()  
    data = serializers.JSONField()

    class Meta:
        model = CocoaContracts
        fields = ('id', 'data')
