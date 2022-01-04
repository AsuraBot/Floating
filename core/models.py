from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator


class MainInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    icon = models.CharField(max_length=50, verbose_name="Иконка")

    class Meta:
        verbose_name = "Главная информация"
        verbose_name_plural = "Главная информация"

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(verbose_name="Название услуги", max_length=100)
    duration = models.PositiveSmallIntegerField(verbose_name="Продолжительность")
    description = models.CharField(verbose_name="Описание", max_length=150)
    info = models.TextField(verbose_name="Инфо", max_length=150)
    price = models.PositiveIntegerField(verbose_name="Цена")
    icon = models.CharField(verbose_name="Иконка", max_length=50, null=True, blank=True)
    on_main = models.BooleanField(verbose_name="Выводить на главной", default=False)
    is_active = models.BooleanField(verbose_name="Доступно", default=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class Promotion(models.Model):
    ABON = "abon"
    CARD = "card"
    GIFT = "gift"
    PROMOTION_TYPES = (
        (ABON, "Абонемент"),
        (CARD, "Клубная карта"),
        (GIFT, "Подарочный сертификат"),
    )
    type = models.CharField(verbose_name="Тип", max_length=4, choices=PROMOTION_TYPES)
    name = models.CharField(verbose_name="Название", max_length=100)
    duration = models.PositiveSmallIntegerField(verbose_name="Продолжительность")
    description = models.CharField(verbose_name="Описание", max_length=150)
    price = models.PositiveIntegerField(verbose_name="Цена")
    is_active = models.BooleanField(verbose_name="Доступно", default=True)

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=50)
    text = models.TextField(verbose_name="Текст отзыва", max_length=1000)
    rating = models.PositiveSmallIntegerField(
        verbose_name="Рейтинг", validators=(MaxValueValidator(10),)
    )
    date = models.DateTimeField(verbose_name="Дата отзыва", auto_now_add=True)
    moderated = models.BooleanField(verbose_name="Отзыв проверен", default=False)
    on_main = models.BooleanField(verbose_name="Выводить на главной", default=False)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.EmailField(verbose_name="Почта", max_length=50)
    phone = models.CharField(verbose_name="Телефон", max_length=20)
    address = models.CharField(verbose_name="Адрес", max_length=70)
    schedule = models.CharField(verbose_name="График работы", max_length=150)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.email


class Effect(models.Model):
    name = models.CharField(verbose_name="Эффект", max_length=50)
    text = models.TextField(verbose_name="Описание эффекта", max_length=250)
    image = models.ImageField(verbose_name="Фото")
    on_main = models.BooleanField(verbose_name="Выводить на главной", default=False)

    class Meta:
        verbose_name = "Эффект"
        verbose_name_plural = "Эффекты"

    def __str__(self):
        return self.name


class HowItWork(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    text = models.TextField(verbose_name="Текст", max_length=1000)
    on_main = models.BooleanField(verbose_name="Выводить на главной", default=False)

    class Meta:
        verbose_name = "Как это работает"
        verbose_name_plural = "Как это работает"

    def __str__(self):
        return self.name
