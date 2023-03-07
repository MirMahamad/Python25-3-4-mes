from django.db import models
from django.contrib.auth.models import User
ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIPClient, "VIPClient"),
    (CLIENT, "CLIENT")
)

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
    (OTHER, "OTHER")
)

KYRGYZSTAN = 1
RUSSIA = 2
KAZAKHSTAN = 3

COUNTRY_TYPE = (
    (KYRGYZSTAN, "KYRGYZSTAN"),
    (RUSSIA, "RUSSIA"),
    (KAZAKHSTAN, "KAZAKHSTAN")
)

YES = 1
NO = 2

GAME_TYPE = (
    (YES, "YES"),
    (NO, "NO")
)


class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип Пользователя')
    phone_number = models.CharField('номер телефона', max_length=20)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Пол')
    country = models.IntegerField(choices=COUNTRY_TYPE, verbose_name='Страна')
    region = models.PositiveIntegerField()
    mail = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    game = models.IntegerField(choices=GAME_TYPE, verbose_name='Играете ли в игры')

