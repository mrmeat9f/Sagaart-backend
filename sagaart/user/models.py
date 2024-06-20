from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from ..sagaart.values import (
    MAX_LENGTH_USER,
    MAX_LENGTH_TEXT,
)


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'id',
        'username',
        'first_name',
        'last_name',
    ]
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
    )
    first_name = models.CharField(
        'Имя',
        max_length=MAX_LENGTH_USER,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=MAX_LENGTH_USER,
    )
    middle_name = models.CharField(
        'Отчество',
        max_length=MAX_LENGTH_USER,
    )
    nick_name = models.CharField(
        'Псевдоним',
        unique=True,
        max_length=MAX_LENGTH_USER,
    )
    biograthy = models.TextField(
        'Биография автора',
        max_length=MAX_LENGTH_TEXT,
    )
    year_of_birth = models.DateField(
        'Год рождения'
    )
    place_of_birth = models.CharField(
        'Город рождения',
        max_length=MAX_LENGTH_USER,
    )
    residence_city = models.CharField(
        'Город проживания',
        max_length=MAX_LENGTH_USER,
    )
    education = models.CharField(
        'Образование',
        max_length=MAX_LENGTH_USER,
    )
    art_education = models.CharField(
        'Художественное образование',
        max_length=MAX_LENGTH_USER,
    )
    teaching_experience = models.CharField(
        'Опыт преподавания',
        max_length=MAX_LENGTH_USER,
    )
    personal_style = models.CharField(
        'Персональный стиль',
        max_length=MAX_LENGTH_USER,
    )
    solo_shows = models.TextField(
        'Персональные выставки',
        max_length=MAX_LENGTH_TEXT,
    )
    solo_shows_gallery = models.TextField(
        'Галлереи персональнх выставкок',
        max_length=MAX_LENGTH_TEXT,
    )
    group_shows = models.TextField(
        'Групповые выставки',
        max_length=MAX_LENGTH_TEXT,
    )
    group_shows_gallery = models.TextField(
        'Галереи групповых выставок',
        max_length=MAX_LENGTH_TEXT,
    )
    group_shows_artist = models.TextField(
        'Участники групповых выставок',
        max_length=MAX_LENGTH_TEXT,
    )
    collected_private = models.TextField(
        'collected private',
        max_length=MAX_LENGTH_TEXT,
    )
    collected_major = models.TextField(
        'Полученные призовые места',
        max_length=MAX_LENGTH_TEXT,
    )
    winner = models.TextField(
        'Победитель',
        max_length=MAX_LENGTH_TEXT,
    )
    social_network = models.TextField(
        'Социальные сети',
        max_length=MAX_LENGTH_TEXT,
    )
    avg_price = models.TextField(
        'Средняя цена',
        max_length=MAX_LENGTH_TEXT,
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def str(self):
        return self.username