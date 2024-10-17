import stripe
from djangoProject9.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_price(amount):

    stripe.Price.create(
        currency="usd",
        unit_amount=1000,
        recurring={"interval": "month"},
        product_data={"name": "Gold Plan"},
    )
