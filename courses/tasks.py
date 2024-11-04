from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from djangoProject9.settings import EMAIL_HOST_USER
from users.models import User


@shared_task
def send_info_about_like(email):
    """Отправляет сообщение пользователю о лайках"""
    send_mail('Новый лайк', 'Вашему курсу поставили лайк', EMAIL_HOST_USER, [email])


@shared_task
def send_email_about_course_update(emails):
    """Отправляет сообщение подписчикам об изменении курса"""
    send_mail('Курс обновлён', 'Информация в курсе обновлена', EMAIL_HOST_USER, emails)


@shared_task
def block_if_not_active():
    """Блокирует неактивных пользователей"""
    one_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month_ago, is_active=True)
    inactive_users.update(is_active=False)
