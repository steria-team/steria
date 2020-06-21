from typing import Dict

from flask_restful import abort
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
        address: str = args['address']
        try:
            data: HouseData = HouseData.from_carto(address)
        except Exception:
            msg: str = f'Could not get information at this address: {address}'
            abort(
                http_status_code=500,
                message=dict(
                    Error=msg
                )
            )
        return {
            **data.get_dict()
        }
