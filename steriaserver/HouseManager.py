from flask_restful import Api, Resource, reqparse
from flask import Response
import random
import requests
import json
from urllib import parse

# Вызов API carto по адресу
# apiUrl = f'https://nslavin.carto.com/api/v2/sql?q=select%20*%20from%20public.saint_pv4_050620%20where%20r_adress%20like{r_adress}'
# reqAddress = requests.get(apiUrl)
# print("Status code:", reqAddress.status_code)
# responseJson = reqAddress.json()



# Сырой пример api сервиса для фронта.




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







    # def post(self, r_adress):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument("author")
    #     parser.add_argument("quote")
    #     params = parser.parse_args()
    #     for quote in ai_quotes:
    #         if(id == quote["r_adress"]):
    #             return f"Quote with r_adress {r_adress} already exists", 400
    #     quote = {
    #         "r_adress": str(r_adress),
    #         "author": params["author"],
    #         "quote": params["quote"]
    #     }
    #     ai_quotes.append(quote)
    #     return quote, 201
