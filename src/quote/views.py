from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuoteSerializer
from .service import QuoteService
from .validator import Validator

"""
A view function takes in information from a request, prepares the data needed to generate a page, and then sends
the data back to the browser, often by using a template that defines what the page will look like.
"""


class QuoteViewSet(APIView):

    def get_queryset(self):
        params = self.request.query_params   # QueryDict in response
        return params

    def get(self, request):
        queryset = self.get_queryset()
        quote_service = QuoteService(queryset)
        validator = Validator(queryset)
        try:
            validator.is_valid_get_query_params()
        except Exception as e:
            return Response('%s' % e.args[0], status=status.HTTP_400_BAD_REQUEST)
        exchange_amount = quote_service.get_exchange_amount()

        return Response({"get_exchange_amount": exchange_amount})

    def post(self, request):
        queryset = self.get_queryset()
        serializer = QuoteSerializer(data=queryset)
        # without validating the data, you can not write the data into the Database. The raise_exception argument
        # will raise the exception if there are validation errors
        if serializer.is_valid(raise_exception=True):
            # call .save() to return an object instance, based on the validated data.
            serializer.save()
            return Response(serializer.data)
