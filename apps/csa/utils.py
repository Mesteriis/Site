import csv
from datetime import datetime
from . import models


def monthDelta(date, delta):
    m, y = (date.month + delta) % 12, date.year + ((date.month) + delta - 1) // 12
    if not m: m = 12
    d = min(date.day, [31,
                       29 if y % 4 == 0 and not y % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return date.replace(day=d, month=m, year=y)


def get_data_online():
    db_map = {'uid': 'uid', 'id': 'vehicleID', 'tc': 'vehicleName', 'login': 'serverLogin'}
    table = models.db_online.objects.using('mssql_Vehicles').raw('exec spAllVehicles', translations=db_map)

    count_list = len(table)
    arr_list = ['']
    for r in table:
        count = 0

        list_online_in_base = dict(ID='', Number='', login='', IMEI='', phone='')
        for k in dict(r.__dict__):
            if count == 2:
                list_online_in_base['ID'] = int(getattr(r, k))
                # print(str(getattr(r, k)))
            elif count == 3:
                list_online_in_base['Number'] = str(getattr(r, k))
            elif count == 4:
                list_online_in_base['login'] = str(getattr(r, k))
                arr_list.append(list_online_in_base)
            count += 1
    return {
        # 'list_online': sorted(arr_list, key=lambda x: x['ID']),
        'list_online': arr_list,
        'count': count_list
    }


def get_data_online_dict():
    db_map = {'uid': 'uid', 'id': 'vehicleID', 'tc': 'vehicleName', 'login': 'serverLogin'}
    table = models.db_online.objects.using('mssql_Vehicles').raw('exec spAllVehicles', translations=db_map)
    count_list = len(table)
    arr_list = ['']
    dict_online = {}
    list_online_in_base = dict(ID='', Number='', login='', IMEI='', phone='', link1c='')
    isDouble = False
    for r in table:
        count = 0
        for k in dict(r.__dict__):
            if count == 2:
                dict_online[getattr(r, k)]['ID'] = int(getattr(r, k))
            elif count == 3:
                dict_online[getattr(r, k)]['Number'] = (getattr(r, k))
            elif count == 4:
                if dict_online[getattr(r, k)]['login']:
                    dict_online[getattr(r, k)]['login'] += dict_online[getattr(r, k)]['login'] + ', ' + (getattr(r, k))
                else:
                    dict_online[getattr(r, k)]['login'] = (getattr(r, k))
            count += 1
    return {
        # 'list_online': sorted(arr_list, key=lambda x: x['ID']),
        'list_online': dict_online,
        'count': count_list
    }


def read_data_1c(filename):
    """
    Метод парсит данные полученные с 1с с жёсткой шапкой
    (Организация; Партнер; ИНН; КПП; ТС; ГосНомер; ИД; Активно; ОкончаниеНачисления; НомерНачисления; ДатаНачисления;
    Сумманачисления;НомерСчета;ДатаСчет;)
    :param filename: str() путь к файлу
    :return: lsit () {
        'info': {
            'READ': count, Сколько всего прочитано с файла строк (кол-во)
            'NO_ID': len(arr_1c_noID ), Записи без ID (кол-во)
            'BLOCK': len(arr_1c_block ), Записи которые находятся в блоке (кол-во)
            'ERROR': len(arr_1c_error ), записи с ошибками в дате, в текущей реализации с некорректной датой (кол-во)
            'OTHER': len(arr_1c_other ), записи которые на первый взгляд кажутся достоверными (кол-во)
            'HEADER': headers, шапка таблицы
            'IDENT': len(arr_1c_error) + len(arr_1c_block) + len(arr_1c_noID) + len(arr_1c_other), сколько всего распознано данных
       } , листы данных для выгрузки в веб
        'other': arr_1c_other,
        'noID': arr_1c_noID,
        'block': arr_1c_block,
        'error': arr_1c_error
    }
    """
    arr_1c_other = list()  # на первый взгляд нормальные
    arr_1c_noID = list()  # нет id
    arr_1c_block = list()  # в блоке по данным 1с
    arr_1c_error = list()  # ошибки в данных
    count = 0
    dict_org = dict()
    dict_part = dict()
    with open(filename) as f:
        reader = csv.reader(f, delimiter=';')
        headers = next(reader)
        for row in reader:
            count += 1
            tmpDict = dict()
            tmpDict['org'] = row[0]
            dict_org[row[0]] = row[0]
            tmpDict['part'] = row[1]
            dict_part[row[1]] = row[1]
            tmpDict['inn'] = row[2]
            tmpDict['kpp'] = row[3]
            tmpDict['avto'] = row[4]
            tmpDict['a_number'] = row[5]
            tmpDict['id'] = row[6]
            tmpDict['isActive'] = row[7]
            tmpDict['end_nach'] = row[8].split(' ')[0]
            tmpDict['num_nach'] = row[9]
            tmpDict['date_nach'] = row[10].split(' ')[0]
            tmpDict['sum_nach'] = row[11]
            tmpDict['num_pay'] = row[12]
            tmpDict['date_pay'] = row[13].split(' ')[0]

            if tmpDict['isActive'] == 'Нет':
                arr_1c_block.append(tmpDict)
                continue

            if not tmpDict['id']:
                arr_1c_noID.append(tmpDict)
                continue

            if tmpDict['date_nach'] and tmpDict['date_pay']:
                if len(tmpDict['date_pay'].split('.')[0]) == 2:
                    try:
                        tmpDict['date_nach'] = datetime.strptime(tmpDict['date_nach'], '%d.%m.%Y').date()
                        tmpDict['date_pay'] = datetime.strptime(tmpDict['date_pay'], '%d.%m.%Y').date()
                    except ValueError:
                        arr_1c_error.append(tmpDict)
                elif len(tmpDict['date_pay'].split('.')[0]) == 4:
                    if tmpDict['date_pay'].split('.')[0][0:2] == '00':
                        arr_1c_error.append(tmpDict)
                        continue
                    try:
                        tmpDict['date_nach'] = datetime.strptime(tmpDict['date_nach'], '%Y.%m.%d').date()
                        tmpDict['date_pay'] = datetime.strptime(tmpDict['date_pay'], '%Y.%m.%d').date()
                    except ValueError:
                        arr_1c_error.append(tmpDict)
            arr_1c_other.append(tmpDict)

    print('Нет ИД', len(arr_1c_noID))
    print('блокирован', len(arr_1c_block))
    print('ошибка импорта', len(arr_1c_error))
    print('Вроде нормальные', len(arr_1c_other))
    return {
        'error_fnc': '',
        'info': {
            'READ': count,
            'NO_ID': len(arr_1c_noID),
            'BLOCK': len(arr_1c_block),
            'ERROR': len(arr_1c_error),
            'OTHER': len(arr_1c_other),
            'HEADER': headers,
            'IDENT': len(arr_1c_error) + len(arr_1c_block) + len(arr_1c_noID) + len(arr_1c_other),
            'dict_org': dict_org,
            'dict_part': dict_part
        },
        'other': arr_1c_other,
        'noID': arr_1c_noID,
        'block': arr_1c_block,
        'error': arr_1c_error
    }
