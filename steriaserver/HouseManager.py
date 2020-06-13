from flask_restful import Api, Resource, reqparse
from flask import Response
import random
import requests
import json
from urllib import parse


class Quote(Resource):
    def get(self, r_adress):
        if r_adress == 0:
            return "Quote not found", 404
        return self.callApi(r_adress)

    def callApi(self, r_adress):
        print(r_adress)
        query = {'q': f"select * from public.saint_pv4_050620 where r_adress like '%{r_adress}%' or r_adress='{r_adress}'"}
        print(query)
        params = parse.urlencode(query)
        apiUrl = 'https://nslavin.carto.com/api/v2/sql?' + params

        print(apiUrl)
        reqAddress = requests.get(apiUrl)
        print("Status code:", reqAddress.status_code)
        print(reqAddress.text)
        return reqAddress.json()

