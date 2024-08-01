from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = {'blank': True, 'null': True}


class Reader(AbstractUser):
    """
    Модель читателя библиотеки
    """

    username = models.CharField(max_length=20, unique=True, verbose_name='логин')
    first_name = models.CharField(max_length=20, verbose_name='имя')
    last_name = models.CharField(max_length=20, verbose_name='фамилия')
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='readers/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='номер телефона', **NULLABLE)
    address = models.TextField(verbose_name='адрес')
    is_active = None

    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'читатель'
        verbose_name_plural = 'читатели'
