from django.contrib.auth.models import User
from django.db import models

# for request bank account
import json
import requests
# import rest


# Create your models here.
from django.utils import timezone


def getBalance(idFirm):
    bal = AccountingList.objects.all().filter(idClient=idFirm).latest('id')
    return bal.SaldoAfter


def waitInvoiceStatus(invoice):
    idFirm = 0
    sum = 0
    return idFirm, sum


class AccountingList(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата операции')
    SaldoBefore = models.DecimalField(max_digits=8, decimal_places=2, default='0.00')
    DEBET = 'dt'
    CREDIT = 'ct'
    PROMISED = 'pr'
    typesActivity = (
        (DEBET, 'Приход'),
        (CREDIT, 'Расход'),
        (PROMISED, 'Обещанный платеж'),
    )
    typeActivity = models.CharField(max_length=2, choices=typesActivity, default=CREDIT, verbose_name='Тип операции')
    sum = models.PositiveIntegerField(verbose_name='Сумма операции')
    SaldoAfter = models.DecimalField(max_digits=8, decimal_places=2, default='0.00')
    Comment = models.CharField(max_length=300, verbose_name='Комментарий блокировки')
    # FIXME DO_NOTHING сменить на CASCADE когда будут клиенты
    idClient = models.ForeignKey('ClientFirm', on_delete=models.DO_NOTHING, verbose_name='Фирма клиента', default=None)
    # FIXME DO_NOTHING сменить на CASCADE когда будут клиенты
    idPromisedPayment = models.ForeignKey('promisedPayment', on_delete=models.DO_NOTHING,
                                          verbose_name='Обещанный платеж', default=None)
    startDate = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    endDate = models.DateTimeField(auto_now=False, auto_now_add=False, default=None)
    FINANSE = 'fn'
    TECHNICAL = 'tn'
    REST = 'rs'
    typesBlock = (
        (FINANSE, 'Финансовая блокировка'),
        (TECHNICAL, 'Техническая блокировка'),
        (REST, 'Остальное'),
    )
    # подумать может быть в отдельную таблицу
    typeBlock = models.CharField(max_length=2, choices=typesBlock, default=FINANSE, verbose_name='Тип блокировки')
    isBlock = models.BooleanField(default=False, verbose_name='Заблокирован')
    dateBlock = models.DateField(verbose_name='Дата будущей блокировки', default='')
    BlockComment = models.CharField(max_length=300, verbose_name='Комментарий блокировки')

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.created = timezone.now ()
    #     self.modified = timezone.now ()
    #     return super (User, self).save ( *args, **kwargs )


class ClientFirm(models.Model):
    name = models.CharField(max_length=120)


class promisedPayment(models.Model):
    name = models.CharField(max_length=120)
