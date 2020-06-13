from dataclasses import dataclass
from typing import Dict

import flask
from flask import testing
from flask import wrappers
import pytest


@dataclass(init=True)
class HouseData:
    r_name: str
    r_years_string: str
    r_adress: str
    r_architect: str
    r_style: str


def test_smoke_test(client):
    res: wrappers.Response = client.get('/test')
    assert res.data.decode('utf-8') == 'test'


house_full_address: HouseData = HouseData(
    r_adress='Обводный кан.  10',
    r_name='Масляный мост',
    r_years_string='1984',
    r_architect='Современный',
    r_style='Современный'
)

house_address_contains: HouseData = HouseData(
    r_adress='197022, г.Санкт-Петербург, '
             'Каменноостровский проспект, дом 59, литера А',
    r_name='Доходный дом И. Д. Агафонова',
    r_years_string='1908-1909',
    r_architect='Модерн',
    r_style='Модерн'
)


@pytest.mark.parametrize(
    'address, expected_data',
    [('Обводный кан. 10', house_full_address),
     ('Каменноостровский проспект, дом 59', house_address_contains)])
def test_get_address_data(client: testing.FlaskClient,
                          address: str,
                          expected_data: HouseData):
    res: wrappers.Response = client.get('/address',
                                        json={'version': '0.1.0',
                                              'house_data': {
                                                  'address': address}
                                              })
    params: Dict = flask.json.loads(res.get_data())['house_data']

    for name in params:
        assert params[name] == expected_data.__dict__[name], f'name={name}'
