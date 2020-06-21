from typing import Dict

from flask_restful import reqparse
from flask_restful import Resource
from steriaserver.houselib import HouseData
# from steriaserver import api

parser = reqparse.RequestParser()
parser.add_argument(
    'address',
    dest='address',
    type=str,
    required=True
)


# @api.resource('/v1/house')
class HouseResource(Resource):

    def get(self):
        args: Dict[str, str] = parser.parse_args()
        try:
            data: HouseData = HouseData.from_carto(args['address'])
        except Exception:
            return 'Error', 500
        return {
            **data.get_dict()
        }
