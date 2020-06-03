class DialogflowAPI(object):
    def __init__(self):
        pass

    @staticmethod
    def get_error_event(fulfillmentMessages, error_type: str, error_text: str) -> dict:
        return {
            "fulfillmentMessages": fulfillmentMessages,
            "followupEventInput": {
                "name": "event_error",
                "parameters": {
                    "error_type": error_type,
                    "error_text": error_text
                },
                "languageCode": "en-US"
            }
        }

    @staticmethod
    def get_error_context(session: str, error_type: str, error_text: str) -> dict:
        return {
            "followupEventInput": {
                "name": "event_error",
                "parameters": {
                    "error_type": error_type,
                    "error_text": error_text
                },
                "languageCode": "en-US"
            },
            "outputContexts": [
                {
                    "name": f"{session}/contexts/ErrorData",
                    "lifespanCount": 5,
                    "parameters": {
                        "error_type": error_type,
                        "error_text": error_text
                    }
                }
            ]
        }
