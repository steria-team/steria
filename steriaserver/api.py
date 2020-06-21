from flask_restful import Resource
from steriaserver.houselib import HouseData


class HouseResource(Resource):

    def get(self, address: str):

        try:
            data: HouseData = HouseData.from_carto(address)
        except Exception:
            return 'Error', 500
        return {
            **data.get_dict()
        }
