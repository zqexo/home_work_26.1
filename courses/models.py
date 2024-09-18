from django.db import models


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

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
