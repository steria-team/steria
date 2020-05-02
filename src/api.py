# coding: utf-8
# Импортирует поддержку UTF-8.
# from __future__ import absolute_import
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
import typing

import os
import pathlib

from flask import Flask, request
# from flask_cors import CORS

# from . import house

import house

app = Flask(__name__)
# CORS(app)
port = int(os.environ.get("PORT", 5000))

DIR_SCRIPT: pathlib.Path = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))

# Хранилище данных о сессиях.
sessionStorage: typing.Dict[str,  house.House] = {}

# @app.after_request
# def after_request(response):
#     header = response.headers
#     header['Access-Control-Allow-Origin'] = 'https://alice-dev.vitalets.xyz'
#     return response


@app.route('/test')
def test():
    return "test"

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


def handle_dialog(req, res):
    user_id = req['session']['user_id']

    # if req['session']['new']:
    # if sessionStorage.get(user_id) is None:
    #     # Это новый пользователь.
    #     # Инициализируем сессию и поприветствуем его.
    #     sessionStorage[user_id]: typing.Dict[house.House] = house.House()
    #     res['response']['text'] = sessionStorage[user_id].help()
    #     return
    # else:
    #
    #     user_data: house.House = sessionStorage[user_id]
    #     user_answer: str = req['request']['original_utterance'].lower()
    #
    #     if user_answer == 'сброс':
    #         res['response']['text'] = sessionStorage[user_id].reset()
    #
    #     user_data.parse_response(text=user_answer)
    #     res['response']['text'] = user_data.answer()
    res['response']['text'] = 'test'

    return


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)