from datetime import datetime
import json


def sort_key(item):
    '''
    Ключ для сортировки
    списка словарей по дате
    '''
    return item.get('date') or ''


def load_sorted_operations():
    '''
    Считывает файл json.
    Сортирует список словарей по дате.
    Возвращает список из 5ти последних операций
    '''
    with open('operations.json', 'rt', encoding='utf-8') as file:
        operations = json.load(file)
        sorted_operations = sorted(operations, key=sort_key, reverse=True)
        list_of_five = []
        for i in sorted_operations:
            if i.get('state') == 'EXECUTED':
                if len(list_of_five) < 5:
                    list_of_five.append(i)
        return list_of_five


def get_date(op_date):
    '''
    Принимает дату в формате год-месяц-день
    Возвращает дату в формате день.месяц.год
    '''
    ymd = op_date[0:10]
    the_date = datetime.strptime(ymd, '%Y-%m-%d')
    return the_date.strftime('%d.%m.%Y')


def get_where_from(where_from):
    '''
    Принимает счет отправителя.
    Возвращает замаскированный звездами счет.
    '''
    word = "".join("" if el.isdigit() else el for el in where_from)
    number = "".join(el if el.isdigit() else "" for el in where_from)
    stars = len(number) - 10
    star_number = number[:6] + stars * '*' + number[-4:]
    sep_number = [star_number[i:i + 4] for i in range(0, len(star_number), 4)]
    where_from = word + ' '.join(sep_number)
    return where_from


def get_where_to(where_to):
    '''
    Принимает счет получателя.
    Возвращает замаскированный звездами счет.
    '''
    word = "".join("" if el.isdigit() else el for el in where_to)
    number = "".join(el if el.isdigit() else "" for el in where_to)
    # stars = len(number) - 4
    star_number = 2 * '*' + number[-4:]
    where_to = word + ''.join(star_number)
    return where_to