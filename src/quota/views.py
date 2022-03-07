from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Quota
from .serializers import QuotaSerializer


class QuotaViewSet(APIView):

    def get_queryset(self):
        parameter = self.request.query_params
        return parameter

    def get(self, request):
        queryset = self.get_queryset()
        return Response(queryset)

    def post(self, request):
        queryset = self.get_queryset()
        serializer = QuotaSerializer(data=queryset)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)








