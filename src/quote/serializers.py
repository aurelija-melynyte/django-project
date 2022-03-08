from rest_framework import serializers
from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    """class that will manage serialization and deserialization from JSON."""
    class Meta:
        """
        The Meta class holds extra information for managing a model
        params:
        model - the model for Serializer
        fields - a tuple of field names to be included in the serialization
        """
        model = Quote
        fields = ('id', 'currency')