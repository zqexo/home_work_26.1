from datetime import datetime

import requests
import stripe
from forex_python.converter import CurrencyRates

from djangoProject9.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def convert_rub_to_dollars(amount):
    """Конвертирует рубли в доллары"""

    return int(amount // 90)


def create_stripe_price(amount):
    """Создаёт цену в страйпе"""

    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": "Donation"},
    )


def create_stripe_session(price):
    """Создаёт сессию на оплату в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[
            {
                "price": price.get("id"),
                "quantity": 1,
            }
        ],
        mode="payment",
    )
    return session.get("id"), session.get("url")
