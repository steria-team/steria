from typing import Dict
from typing import Union

from flask_restful import abort
from flask_restful import fields
from flask_restful import marshal_with
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


resource_fields: Dict[str, fields.String] = {
    'r_adress': fields.String,
    'r_name': fields.String,
    'r_architect': fields.String,
    # 'r_cw_url': fields.String,
    'r_style': fields.String,
    'r_years_string': fields.String
}

# @api.resource('/v1/house')
class HouseResource(Resource):

    @marshal_with(resource_fields)
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
        return data

