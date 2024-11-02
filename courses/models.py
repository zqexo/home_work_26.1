from django.db import models

import users
from djangoProject9 import settings


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
        help_text="Введите название",
    )
    preview = models.ImageField(
        upload_to="courses/previews",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Выберите фото",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Создатель",
    )

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        verbose_name="Лайки",
        related_name="user_likes",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Курс",
        help_text="Выберите курс",
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Введите описание",
    )
    preview = models.ImageField(
        upload_to="courses/previews",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Выберите фото",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Создатель",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Подписка"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="Подписка"
    )

    class Meta:
        unique_together = (
            "user",
            "course",
        )  # Обеспечим уникальность подписки для пользователя и курса
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f"{self.user.email} subscribed to {self.course.title}"
