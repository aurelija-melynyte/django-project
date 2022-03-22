from django.core.exceptions import ValidationError
from .constants import SUPPORTED_CURRENCIES


class Validator:
    def __init__(self, params):
        self.params = params

    def is_valid_get_query_params(self):
        base_currency = self.params['base_currency']
        quote_currency = self.params['quote_currency']
        base_amount = self.params['base_amount']

        if base_currency not in SUPPORTED_CURRENCIES:
            raise ValidationError({"message": "Invalid base_currency input, possible currencies: USD, EUR, GBP, ILS "})
        if quote_currency not in SUPPORTED_CURRENCIES[base_currency]:
            raise ValidationError({"message": "Invalid quote_currency input, possible currencies: USD, EUR, GBP, ILS"})
        try:
            int(base_amount)
        except ValidationError:
            raise ValidationError({'message': "Base amount should be integer"})
        if int(base_amount) < 0:
            raise ValidationError({"message": "Base amount should not be negative"})
