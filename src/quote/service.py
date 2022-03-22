from .constants import SUPPORTED_CURRENCIES


class QuoteService:
    def __init__(self, params):
        self.params = params

    def get_exchange_amount(self):
        base_currency = self.params['base_currency']
        quote_currency = self.params['quote_currency']
        base_amount = self.params['base_amount']

        return int(base_amount)/100 * SUPPORTED_CURRENCIES[base_currency][quote_currency]
