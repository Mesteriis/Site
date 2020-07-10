from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json

from sql_server import pyodbc

x1 = dict(vehicleID='312312', vehicleName='а 123 аа 36', serverLogin='wialon')
x2 = dict(vehicleID='15312319', vehicleName='а 123 аа 36', serverLogin='wialon')
x3 = dict(vehicleID='14234213459', vehicleName='а 123 аа 36', serverLogin='wialon')
x4 = dict(vehicleID='159', vehicleName='а 123 аа 36', serverLogin='wialon')
x5 = dict(vehicleID='159', vehicleName='а 123 аа 36', serverLogin='wialon')
arr_online = list()
arr_online.append(x1)
arr_online.append(x2)
arr_online.append(x3)
arr_online.append(x4)
arr_online.append(x5)

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


# Create your views here.
@login_required(login_url="/login/")
def csa(request):
    # conn = pyodbc
    # conn = pyodbc.connect(
    #     'DRIVER={ODBC Driver 17 for SQL Server};SERVER=195.19.10.176\SQLEXPRESS;DATABASE=support;UID=avm;PWD=avm123')

    context = {
        'list_online': arr_online,
        'list_online_size': len(arr_online),
        'list_1c': arr_1c,
        'list_1c_size': len(arr_1c),
    }
    templates_name = 'csa/index.html'

    return render(request, templates_name, context)


def get_data_online(request):
