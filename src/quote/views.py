from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuoteSerializer

"""
A view function takes in information from a request, prepares the data needed to generate a page, and then sends
the data back to the browser, often by using a template that defines what the page will look like.
"""


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
