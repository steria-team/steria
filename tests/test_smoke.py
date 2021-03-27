from dataclasses import dataclass
from typing import Dict




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
    r_adress='проспект Медиков10 к2',
    r_name='',
    r_years_string='2015',
    r_architect=None,
    r_style=None
)

house_address_contains: HouseData = HouseData(
    r_adress='197022, г.Санкт-Петербург, '
             'Каменноостровский проспект, дом 59, литера А',
    r_name='Доходный дом И. Д. Агафонова',
    r_years_string='1908-1909',
    r_architect='Мульханов П. М.',
    r_style='Модерн'
)


@pytest.mark.parametrize(
    'address, expected_data',
    [('проспект Медиков10 к2', house_full_address),
     ('Каменноостровский проспект, дом 59', house_address_contains)]
)
def test_get_address_data(client: testing.FlaskClient,
                          address: str,
                          expected_data: HouseData):

    res: wrappers.Response = client.get(f'/v1/house?address={address}')

    params: Dict = flask.json.loads(res.get_data())

    for name in params:
        assert params[name] == expected_data.__dict__[name], f'name={name}'


def test_required_params_error(client: testing.FlaskClient):
    response_data: Dict[str, str] = flask.json.loads(
        client.get('/v1/house').get_data()
    )

    assert len(response_data.keys()) == 1
    assert response_data['message'] == {
        'address': 'Missing required parameter in the JSON body or '
                   'the post body or the query string'
    }


def test_bad_value_address_param(client: testing.FlaskClient):
    address: str = 'bad'
    response_data: Dict[str, str] = flask.json.loads(
        client.get(f'/v1/house?address={address}').get_data()
    )

    assert len(response_data.keys()) == 1
    assert response_data['message'] == {
        'Error': f'Could not get information at this address: {address}'
    }

@pytest.mark.parametrize('address', [
                                        'манежный пер 15-17', 
                                        'Манежный пеР 15-17'
                         ])
def test_register_in_request(client: testing.FlaskClient, address: str):
    result = client.get(f'/v1/house?address={address}')
    responce_data: Dict[str, str] = flask.json.loads(
        result.get_data()
    )

    assert result.status_code == 200
