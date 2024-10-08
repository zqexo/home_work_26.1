# import re
from urllib.parse import urlparse

from rest_framework.serializers import ValidationError

forbidden_words = ["ставки", "крипта", "продам", "куплю"]


def validate_forbidden_words(value):
    if value.lower() in forbidden_words:
        raise ValidationError("Использовано запрещённое слово")


def validate_video_link(value):
    """Проверка, что ссылка ведет только на youtube.com."""
    parsed_url = urlparse(value)
    if parsed_url.netloc != "www.youtube.com" and parsed_url.netloc != "youtube.com":
        raise ValidationError(
            "Ссылки на сторонние образовательные платформы или личные сайты запрещены. Используйте только youtube.com."
        )
