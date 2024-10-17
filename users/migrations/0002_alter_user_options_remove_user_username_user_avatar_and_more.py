# Generated by Django 5.1.1 on 2024-09-18 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Выберите фото",
                null=True,
                upload_to="users/avatars",
                verbose_name="Аватар",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="Укажите телефон",
                max_length=35,
                null=True,
                verbose_name="Телефон",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="tg_nick",
            field=models.CharField(
                blank=True,
                help_text="Укажите Telegram",
                max_length=50,
                null=True,
                verbose_name="Телеграм",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                help_text="Введите почту",
                max_length=254,
                unique=True,
                verbose_name="Почта",
            ),
        ),
    ]