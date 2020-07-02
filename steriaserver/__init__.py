from flask import Flask
from flask_cors import CORS
from flask_restful import Api
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

steria_dsn: str = \
    'https://6d5c1c456da44203afe605afda1a4656@o414928.ingest.sentry.io/5305244'

sentry_sdk.init(
    dsn=steria_dsn,
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
api = Api(app)
CORS(app)

from steriaserver import routes # noqa

