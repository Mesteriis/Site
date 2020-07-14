from django.contrib.auth.models import User
from django.db import models


class db_online ( models.Model ):
    uid = models.UUIDField ( primary_key=True )
    vehicleID = models.BigIntegerField ( verbose_name='id', db_column='vehicleID' )
    vehicleName = models.CharField ( max_length=255, verbose_name='ТС', db_column='vehicleName' )
    serverLogin = models.CharField ( max_length=50, verbose_name='Сервер', db_column='serverLogin' )

    class Meta:
        managed = False

    def save(self, *args, **kwargs):
        raise ValueError ( 'Read-only database' )

    def delete(self, *args, **kwargs):
        raise ValueError ( 'Read-only database' )


class custumers_1c_avto(models.Model):
    # Поля из 1с
    org = models.CharField(max_length=50, blank=False, verbose_name='Организация')
    part = models.CharField(max_length=50, blank=False, verbose_name='')
    inn = models.IntegerField( blank=False, verbose_name='')
    kpp = models.IntegerField( blank=True, verbose_name='')
    avto = models.CharField (max_length=20, blank=False, verbose_name="Автомобиль")
    a_number = models.CharField (max_length=20, blank=False, verbose_name="Номер")
    id_1c = models.CharField (max_length=20, blank=False, verbose_name="ID")
    isActive = models.BooleanField (blank=False, verbose_name='Блокировка')
    end_nach = models.DateField(blank=True, verbose_name='Дата блокировки')
    num_last_nach = models.CharField(max_length=20, blank=True, verbose_name='Номер п.н.')
    date_last_nach = models.DateField( blank=True, verbose_name='Дата п.н.')
    sum_last_nach = models.FloatField( blank=True, verbose_name='Сумма п.н.')
    num_last_pay = models.CharField(max_length=20, blank=True, verbose_name='Номер п.с.')
    date_last_pay = models.DateField(blank=True, verbose_name='Дата п.н.')
    raw_DATA = models.TextField(blank=False, verbose_name='Сырые данные')
    # Расчитанные поля

    # Системный поля
    users = models.ManyToManyField(User, blank=True)
    isBlock = models.BooleanField(blank=False, default=False)
    OUR = 'our'
    CLIENT = 'cln'
    status = (
        (OUR, 'Партнер' ),
        (CLIENT, 'Клиент')
    )
    status = models.CharField(max_length=3, choices=status, default=CLIENT, blank=True, verbose_name='')

    class Meta:
        managed = False