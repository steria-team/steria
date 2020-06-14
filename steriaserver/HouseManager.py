from typing import Dict

import requests


class HouseData:

    def __init__(self,
                 r_adress: str, r_name: str,
                 r_architect: str, r_style: str,
                 r_years_string: str, **kwargs):
        self.r_adress: str = r_adress
        self.r_name: str = r_name
        self.r_architect: str = r_architect
        # self.r_cw_url: str = ''
        self.r_style: str = r_style
        self.r_years_string: str = r_years_string

    @staticmethod
    def from_dict(data: Dict[str, str]) -> 'HouseData':
        # todo: Обработка ошибок
        return HouseData(**data)

    def get_json(self) -> Dict[str, str]:
        d = {}
        for key in self.__dict__:
            d[key] = self.__dict__[key]
        return d


class Quote:
    # def get(self, r_adress):
    #     if r_adress == '':
    #         return "Quote not found", 404
    #     return self.callApi(r_adress)

    @staticmethod
    def call_api(r_adress: str) -> Dict[str, str]:
        # print(r_adress)
        query = {'q': f"select * from public.saintpv5_dates where r_adress='{r_adress}' or r_adress like '%{r_adress}%'"}
        # print(query)
        # params = parse.urlencode(query)
        # params = query
        # apiUrl = 'https://nslavin.carto.com/api/v2/sql?' + params
        # todo: почему camelCase? в python api_url
        apiUrl = f'https://nslavin.carto.com/api/v2/sql?q={query["q"]}'

        print(apiUrl)
        reqAddress = requests.get(apiUrl)
        print("Status code:", reqAddress.status_code)
        print(reqAddress.text)

        # todo: проверка ошибок в запросе
        # {'error': ['relation "public.saint_pv4_050620" does not exist']}
        if len(reqAddress.json()['rows']) == 1:
            return reqAddress.json()['rows'][0]
        else:
            raise Exception

        # return reqAddress.json()

