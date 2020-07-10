from django.db import models
from django.contrib.auth.models import User


class Module(models.Model):
    name = models.TextField(max_length=180, verbose_name='Наименование модуля', default='Наименование модуля')
    description = models.TextField(max_length=10000, verbose_name='Описание', default='Описание модуля')
    shortDescription = models.TextField(max_length=300, verbose_name='Короткое описание', default='Короткое описание '
                                                                                                  'модуля')
    pictogram = models.ImageField(verbose_name='Пиктограмма 75Х75', width_field=76, height_field=76)
    promoPictogram = models.ImageField(verbose_name='Промо Изображение 300х300', width_field=301, height_field=301)
    isEnabled = models.BooleanField(default=False)
    serverURL = models.URLField(verbose_name='Сыль на модуль', default='localhost:7000')
    availableUsers = models.ForeignKey(User, on_delete=models.CASCADE) 


