from utils.class_utils import sort_key
from utils.class_utils import load_sorted_operations
from utils.class_utils import get_date
from utils.class_utils import get_where_from
from utils.class_utils import get_where_to


def test_sort_key():
    assert sort_key({
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }) == "2019-08-26T10:50:58.294041"
    assert sort_key({}) == ''


def test_load_sorted_operations():
    assert len(load_sorted_operations()) == 5
    assert load_sorted_operations()[0]['date'] > load_sorted_operations()[4]['date']
    assert load_sorted_operations() == [
        {
            'id': 863064926,
            'state': 'EXECUTED',
            'date': '2019-12-08T22:46:21.935582',
            'operationAmount': {
                'amount': '41096.24',
                'currency': {
                    'name': 'USD',
                    'code': 'USD'
                }
            },
            'description': 'Открытие вклада',
            'to': 'Счет 90424923579946435907'
        },
        {
            'id': 114832369,
            'state': 'EXECUTED',
            'date': '2019-12-07T06:17:14.634890',
            'operationAmount': {
                'amount': '48150.39',
                'currency': {
                    'name': 'USD',
                    'code': 'USD'
                }
            },
            'description': 'Перевод организации',
            'from': 'Visa Classic 2842878893689012',
            'to': 'Счет 35158586384610753655'
        },
        {
            'id': 154927927,
            'state': 'EXECUTED',
            'date': '2019-11-19T09:22:25.899614',
            'operationAmount': {
                'amount': '30153.72',
                'currency': {
                    'name': 'руб.',
                    'code': 'RUB'
                }
            },
            'description': 'Перевод организации',
            'from': 'Maestro 7810846596785568',
            'to': 'Счет 43241152692663622869'
        },
        {
            'id': 482520625,
            'state': 'EXECUTED',
            'date': '2019-11-13T17:38:04.800051',
            'operationAmount': {
                'amount': '62814.53',
                'currency': {
                    'name': 'руб.',
                    'code': 'RUB'
                }
            },
            'description': 'Перевод со счета на счет',
            'from': 'Счет 38611439522855669794',
            'to': 'Счет 46765464282437878125'
        },
        {
            'id': 801684332,
            'state': 'EXECUTED',
            'date': '2019-11-05T12:04:13.781725',
            'operationAmount': {
                'amount': '21344.35',
                'currency': {
                    'name': 'руб.',
                    'code': 'RUB'
                }
            },
            'description': 'Открытие вклада',
            'to': 'Счет 77613226829885488381'
        }
    ]


def test_get_date():
    assert get_date('2019-08-26') == '26.08.2019'


def test_get_where_from():
    assert get_where_from('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'


def test_get_where_to():
    assert get_where_to('Счет 11776614605963066702') == 'Счет ****************6702'
