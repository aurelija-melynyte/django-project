from rest_framework import serializers
from .models import Quota


class QuotaSerializer(serializers.ModelSerializer):
    """class that will manage serialization and deserialization from JSON."""
    class Meta:
        """
        params:
        model - the model for Serializer
        fields - a tuple of field names to be included in the serialization
        """
        model = Quota
        fields = ('id', 'currency')