from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuoteSerializer


class QuoteViewSet(APIView):

    def get_queryset(self):
        parameter = self.request.query_params
        return parameter

    def get(self):
        queryset = self.get_queryset()
        return Response(queryset)

    def post(self):
        queryset = self.get_queryset()
        serializer = QuoteSerializer(data=queryset)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
