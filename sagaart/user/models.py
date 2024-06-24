from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from ..sagaart.values import (
    MAX_LENGTH_USER,
    MAX_LENGTH_TEXT,
)


class User(AbstractUser):
    """"Модель пользователя"""
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
    phone = models.CharField(
        'Номер телефона',
        unique=True,
        max_length=MAX_LENGTH_USER
    )
    icon = models.ImageField(
        upload_to='users/images/',
        verbose_name='Иконка пользователя',
    )
    gender = models.CharField(
        'пол автора',
        max_length=MAX_LENGTH_USER,
    )
    biography = models.TextField(
        'Биография автора',
        max_length=MAX_LENGTH_TEXT,
    )
    year_of_birth = models.PositiveSmallIntegerField(
        'Год рождения',
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
        'хранение в частных коллекциях',
        max_length=MAX_LENGTH_TEXT,
    )
    collected_major = models.TextField(
        'хранение в ведущих музеях',
        max_length=MAX_LENGTH_TEXT,
    )
    winner = models.TextField(
        'ведущие отраслевые награды',
        max_length=MAX_LENGTH_TEXT,
    )
    address = models.TextField(
        'адрес автора',
        max_length=MAX_LENGTH_TEXT,
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def str(self):
        return self.username


class SocialNets(models.Model):
    """"Социальные сети пользователя"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_networks',
        verbose_name='Социальные сети',
    )
    name_nets = models.CharField(
        'название социальной сети',
        max_length=MAX_LENGTH_USER
    )
    account = models.URLField(
        'Ссылка на социальную сеть'
    )

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return f'{self.user.first_name} - {self.account}'


class Education(models.Model):
    """Образование пользователя"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_education',
        verbose_name='Образование пользователя',
    )
    ed_type = models.CharField(
        'Тип образования',
        max_length=MAX_LENGTH_USER
    )
    ed_level = models.CharField(
        'Уровень учебного заведения',
        max_length=MAX_LENGTH_USER,
    )
    ed_name_institute = models.CharField(
        'Наименование учебного заведения',
        max_length=MAX_LENGTH_USER
    )

    class Meta:
        verbose_name = 'Образвание'
        verbose_name_plural = 'Образвание'

    def __str__(self):
        return f'{self.user.first_name} - {self.ed_type}'


class Subscribe(models.Model):
    """Подписка"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_subscribe',
        verbose_name='Подписка пользователя',
    )
    status = models.BooleanField(
        default=False,
    )
    start_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата начала подписки',
    )
    end_date = models.DateTimeField(
        verbose_name='Дата окончания подписки'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.user.first_name} - {self.status}'


class ShoppingList(models.Model):
    """Корзина"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_user',
        verbose_name='Добавил в корзину',
    )
    product = models.ForeignKey(
        Catalog,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Товар в корзине',
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'catalog'],
                name='unique_shopping_cart'
            )
        ]

    def __str__(self):
        return f'{self.user.first_name} - {self.catalog.name}'
