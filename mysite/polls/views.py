from rest_framework import viewsets
from .serializers import CatSerializer
from .models import Cat


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all().order_by('name')
    serializer_class = CatSerializer
