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

    def get(self, request):
        queryset = self.get_queryset()
        return Response(queryset)

    def post(self, request):
        queryset = self.get_queryset()
        serializer = QuoteSerializer(data=queryset)
        # without validating the data, you can not write the data into the Database. The raise_exception argument
        # will raise the exception if there are validation errors
        if serializer.is_valid(raise_exception=True):
            # call .save() to return an object instance, based on the validated data.
            serializer.save()
            return Response(serializer.data)
