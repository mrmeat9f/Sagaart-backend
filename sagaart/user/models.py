from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from sagaart.values import MAX_LENGTH_USER, MAX_LENGHT_TEXT


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['id', 'username', 'first_name', 'last_name']
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
    )
    first_name = models.CharField('Имя', max_length=MAX_LENGTH_USER)
    last_name = models.CharField('Фамилия', max_length=MAX_LENGTH_USER)
    middle_name = models.CharField('Отчество', max_length=MAX_LENGTH_USER)
    nickname = models.CharField('Псевдоним', max_length=MAX_LENGTH_USER)
    biography = models.TextField('Биография автора', max_length=MAX_LENGHT_TEXT)
    birth_year = models.DateField('Год рождения')
    hometown = models.CharField('Город рождения', max_length=MAX_LENGTH_USER)
    residence_city = models.CharField('Город проживания', max_length=MAX_LENGTH_USER)
    education = models.CharField('Образование', max_length=MAX_LENGTH_USER)
    art_education = models.CharField('Художественное образование', max_length=MAX_LENGTH_USER)
    teaching_experience = models.CharField('Опыт преподавания', max_length=MAX_LENGTH_USER)
    personal_style = models.CharField('Персональный стиль', max_length=MAX_LENGTH_USER)
    solo_shows = models.TextField('Персональные выставки', max_length=MAX_LENGHT_TEXT)
    solo_shows_gallery = ...
    group_shows = ...
    group_shows_gallery = ...
    group_shows_artist = ...
    collected_private = ...
    collected_major = ...
    winner = ...
    social_network = ...
    avg_price = ...

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def str(self):
        return self.username