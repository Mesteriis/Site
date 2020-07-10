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
