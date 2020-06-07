import os

from flask_restful import Api
from steriaserver import app
from steriaserver.HouseManager import Quote

# добавил resource к API и задал путь
api = Api(app)
api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:r_adress>")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)