from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from djangoProject9.settings import EMAIL_HOST_USER


@shared_task
def send_info_about_like(email):
    """Отправляет сообщение пользователю о лайках"""
    send_mail('Новый лайк', 'Вашему курсу поставили лайк', EMAIL_HOST_USER, [email])


@shared_task
def send_email_about_birthday(email):
    today = timezone.now().today()
