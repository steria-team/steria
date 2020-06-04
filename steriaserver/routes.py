import json
import logging

from flask import request
from steriaserver import app
from steriaserver import dialogflowapi


@app.route('/test')
def test():
    return 'test'


@app.route('/', methods=['POST'])
def main():
    # Функция получает тело запроса и возвращает ответ.

    request_json = request.get_json(force=True)

    response: dict = {
        'fulfillmentMessages': [
            {
                'text': {
                    'text': [
                        'testing 4.0'
                    ]
                }
            }
        ]
    }
    print(request_json)
    try:
        intent: str = request_json.get('queryResult').get('intent')\
            .get('displayName')
        if intent == 'Version':
            response['fulfillmentMessages']['text']['text'] = '0.0.3'
        elif intent == 'ErrorHelp':
            response: dict = dialogflowapi.DialogflowAPI.get_error_event(
                fulfillmentMessages=request_json.get(
                    'queryResult').get('fulfillmentMessages'),
                error_type='TestError',
                error_text=''
            )
    except Exception as e:
        response: dict = dialogflowapi.DialogflowAPI.get_error_context(
            request_json['session'],
            repr(e),
            ' '.join(e.args)
        )

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )
