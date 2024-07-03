from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from catalog.constants import (
    CHAR_MAX_LENGTH, TEXT_MAX_LENGTH,
    MAX_WEIGHT)


User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        verbose_name='Наименование категории',
        max_length=CHAR_MAX_LENGTH)
    description = models.TextField(
        verbose_name='Описание категории',
        max_length=TEXT_MAX_LENGTH)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        verbose_name='Название товара',
        max_length=CHAR_MAX_LENGTH)
    description = models.TextField(
        verbose_name='Описание товара',
        max_length=TEXT_MAX_LENGTH)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Автор произведения')
    make_date = models.DateField(
        verbose_name='Дата создания',
        validators=[MaxValueValidator(
            limit_value=date.today)])
    size = models.CharField(        # В swagger это поле string?! Уточнить
        verbose_name='Размер товара',
        max_length=CHAR_MAX_LENGTH)
    weight = models.PositiveIntegerField(
        verbose_name='Вес товара',
        validators=[MaxValueValidator(MAX_WEIGHT)])
    edition = models.CharField(
        verbose_name='Версия товара',
        max_length=CHAR_MAX_LENGTH)
    auth_signature = models.BooleanField(
        verbose_name='Подлинность товара',
        default=False)
    photo = models.ImageField(
        upload_to='catalog/images/',
        verbose_name='Фото товара')
    type = models.CharField(
        verbose_name='Тип товара',
        max_length=CHAR_MAX_LENGTH)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория товара')
    status = models.CharField(
        verbose_name='Статус проверки',
        max_length=CHAR_MAX_LENGTH)
    price = models.PositiveIntegerField(
        verbose_name='Цена товара')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

    def __str__(self):
        return self.name
