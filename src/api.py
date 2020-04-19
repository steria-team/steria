# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
import typing

import os
import pathlib


import lxml
from flask import Flask, request
from flask_cors import CORS
from lxml import html

from . import house

app = Flask(__name__)
CORS(app)

DIR_SCRIPT: pathlib.Path = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))

# Хранилище данных о сессиях.
sessionStorage: typing.Dict[str,  house.House] = {}

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = 'https://alice-dev.vitalets.xyz'
    print('header adding')
    return response


@app.route("/", methods=['POST'])
def main():
# Функция получает тело запроса и возвращает ответ.


    request_json = request.get_json(force=True)

    response = {
        "version": request_json['version'],
        "session": request_json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request_json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )


# Функция для непосредственной обработки диалога.
def parse_html(adress: str):
    example_page_path: str = os.path.join(DIR_SCRIPT.parent, 'page_example', 'example.html')
    with open(example_page_path, 'r', encoding='ISO-8859-1') as f:
        text = f.read()
    tree: lxml.html.HtmlElement = html.fromstring(html=text)
    # todo: доделать
    # .//*[@class='address' and text()=', 2']/a[contains(text(), 'Очаковская ул.')]/preceding-sibling::*[@class='cssHouseHead']
    tree.xpath("//div[@class='address' ]/a[contains(text(),'Суво')]")
    return


def handle_dialog(req, res):
    user_id = req['session']['user_id']

    # if req['session']['new']:
    if sessionStorage.get(user_id) is None:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.
        sessionStorage[user_id]: typing.Dict[house.House] = house.House()
        res['response']['text'] = sessionStorage[user_id].ask()
        return
    else:
        if req['request']['original_utterance'].lower() == 'сброс':
            sessionStorage[user_id] = None
            return

        user_data: house.House = sessionStorage[user_id]
        user_data.set_answer(text=req['request']['original_utterance'].lower())
        res['response']['text'] = user_data.answer()

    return


if __name__ == '__main__':
    app.run(debug=True)