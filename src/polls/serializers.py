from rest_framework import serializers

from .models import Cat


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """The Meta class holds extra information for managing a model"""
        model = Cat
        fields = ['name', 'ancient_name']