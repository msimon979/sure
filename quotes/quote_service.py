from django.forms.models import model_to_dict

from lib.cost_calculator import CostCalculator
from quotes.models import Quote
from states.models import State


class QuoteService:
    @staticmethod
    def get_user_quotes(user_id: int) -> Quote:
        quotes = [
            model_to_dict(quote) for quote in Quote.objects.filter(user_id=user_id)
        ]
        return quotes

    @staticmethod
    def update_existing_quote(quote: Quote, state: State) -> None:
        CostCalculator.update_quote(quote, state)
