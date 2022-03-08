from rest_framework import serializers
from .models import Quote

"""Serializers in Django REST Framework are responsible for converting objects into data types understandable
by javascript and front-end frameworks. The two major serializers that are most popularly used are ModelSerializer
and HyperLinkedModelSerialzer."""


class QuoteSerializer(serializers.ModelSerializer):
    """
    class that will manage serialization and deserialization from JSON.
    The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class
    with fields that correspond to the Model fields.
    By default, all the model fields on the class will be mapped to a corresponding serializer fields.
    """

    class Meta:
        """
        The Meta class holds extra information for managing a model
        params:
        model - the model for Serializer
        fields - a tuple of field names to be included in the serialization
        """
        model = Quote
        fields = ('id', 'currency')