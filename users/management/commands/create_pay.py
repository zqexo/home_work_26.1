import datetime

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from users.models import Payment

User = get_user_model()


class Command(BaseCommand):
    help = "Create payment records"

    def handle(self, *args, **kwargs):
        user = User.objects.first()
        course = Course.objects.first()
        lessons = Lesson.objects.first()

        Payment.objects.create(
            user=user,
            payment_date=datetime.date(2024, 9, 1),
            paid_course=course,
            amount=1000.00,
            payment_method="cash",
        )

        Payment.objects.create(
            user=user,
            payment_date=datetime.date(2024, 9, 15),
            paid_lesson=lessons,
            amount=500.00,
            payment_method="transfer",
        )

        self.stdout.write(self.style.SUCCESS("Оплата создана."))
