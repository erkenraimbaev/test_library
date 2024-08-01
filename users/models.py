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
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='номер телефона', **NULLABLE)
    address = models.TextField(verbose_name='адрес')
    is_active = None

    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'читатель'
        verbose_name_plural = 'читатели'


class Librarian(Reader):
    """
    Модель работника библиотеки
    """
    is_active = models.BooleanField(default=True, verbose_name='активный работник')
    personnel_number = models.ForeignKey('self.id', auto_created=True, on_delete=models.DO_NOTHING,
                                         verbose_name='табельный номер')

    def __str__(self):
        return f'{self.username} табельный номер:{self.personnel_number}'

    class Meta:
        verbose_name = 'библиотекарь'
        verbose_name_plural = 'библиотекари'
