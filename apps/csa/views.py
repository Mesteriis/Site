from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models


y1 = dict(org="Мусякаев Р. З. ИП", part="РУССКИЕ ПРОТЕИНЫ ЗАО", inn="3123101276", auto="Ford Х955ОТ 178",
          a_number="Х955ОТ 178", id="15312319", isActive="true", num_nach="172", date_nach="25.06.2020",
          sum_nach="500", num_pay="МРУТ-000159", date_pay="25.06.2020")
y2 = dict(org="Мусякаев Р. З. ИП", part="РУССКИЕ ПРОТЕИНЫ ЗАО", inn="3123101276", auto="Ford Х955ОТ 178",
          a_number="Х955ОТ 178", id="312312", isActive="true", num_nach="172", date_nach="25.06.2020", sum_nach="500",
          num_pay="МРУТ-000159", date_pay="25.06.2020")
y3 = dict(org="Мусякаев Р. З. ИП", part="РУССКИЕ ПРОТЕИНЫ ЗАО", inn="3123101276", auto="Ford Х955ОТ 178",
          a_number="Х955ОТ 178", id="15312319", isActive="true", num_nach="172", date_nach="25.06.2020",
          sum_nach="500", num_pay="МРУТ-000159", date_pay="25.06.2020")
y4 = dict(org="Мусякаев Р. З. ИП", part="РУССКИЕ ПРОТЕИНЫ ЗАО", inn="3123101276", auto="Ford Х955ОТ 178",
          a_number="Х955ОТ 178", id="14234213459", isActive="true", num_nach="172", date_nach="25.06.2020",
          sum_nach="500", num_pay="МРУТ-000159", date_pay="25.06.2020")
y5 = dict(org="Мусякаев Р. З. ИП", part="РУССКИЕ ПРОТЕИНЫ ЗАО", inn="3123101276", auto="Ford Х955ОТ 178",
          a_number="Х955ОТ 178", id="15312319", isActive="true", num_nach="172", date_nach="25.06.2020",
          sum_nach="500", num_pay="МРУТ-000159", date_pay="25.06.2020")
arr_1c = list()
arr_1c.append(y1)
arr_1c.append(y2)
arr_1c.append(y3)
arr_1c.append(y4)
arr_1c.append(y5)


class db(models.Model):
    uid = models.UUIDField(primary_key=True)
    vehicleID = models.BigIntegerField(verbose_name='id', db_column='vehicleID')
    vehicleName = models.CharField(max_length=255, verbose_name='ТС', db_column='vehicleName')
    serverLogin = models.CharField(max_length=50, verbose_name='Сервер', db_column='serverLogin')


# Create your views here.
@login_required(login_url="/login/")
def csa(request):
    # db_map = {'uid': 'uid', 'id': 'vehicleID', 'tc': 'vehicleName', 'login': 'serverLogin'}
    # table = db.objects.using('mssql_Vehicles').raw('exec spAllVehicles', translations=db_map)
    # list_online_in_base = dict(ID='', Number='', login='', IMEI='', phone='')
    #
    # count_list = len(table)
    # arr_list = list()
    # for r in table:
    #     count = 0
    #     for k in dict(r.__dict__):
    #         # print(getattr(r, k))
    #         if count == 0:
    #             pass
    #         if count == 1:
    #             pass
    #         if count == 2:
    #             list_online_in_base['ID'] = str(getattr(r, k))
    #         if count == 3:
    #             list_online_in_base['Number'] = str(getattr(r, k))
    #         if count == 4:
    #             list_online_in_base['login'] = str(getattr(r, k))
    #             print(list_online_in_base)
    #             arr_list.append(list_online_in_base)
    #         count += 1
    #
    # print('размер', len(arr_list))

    context = {
        'list_1c': arr_1c,
        'list_1c_size': len(arr_1c),
    }
    templates_name = 'csa/index.html'

    return render(request, templates_name, context)


def get_data_online(request):
    db_map = {'uid': 'uid', 'id': 'vehicleID', 'tc': 'vehicleName', 'login': 'serverLogin'}
    table = db.objects.using('mssql_Vehicles').raw('exec spAllVehicles', translations=db_map)
    list_online_in_base = dict(ID='', Number='', login='', IMEI='', phone='')

    count_list = len(table)
    arr_list = []
    for r in table:
        count = 0
        for k in dict(r.__dict__):
            if count == 2:
                list_online_in_base['ID'] = str(getattr(r, k))
            elif count == 3:
                list_online_in_base['Number'] = str(getattr(r, k))
            elif count == 4:
                list_online_in_base['login'] = str(getattr(r, k))
                print(list_online_in_base)
                arr_list.append(list_online_in_base)
            count += 1
    return HttpResponse(request, {'list_online': arr_list, 'count': count_list})



