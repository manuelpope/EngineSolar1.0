from  flask import request
from flask_restful import Resource, reqparse
import adapter.model.Models
from engineer.worker.Engineering import Engineer


class LoadResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('designId',
                        type=str,
                        required=None,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('voltage',
                        type=float,
                        required=None,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('current',
                        type=float,
                        required=None,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('quantity',
                        type=int,
                        required=None,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('pf',
                        type=float,
                        required=None,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('workingHoursDay',
                        type=float,
                        required=None,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('workingHoursNight',
                        type=float,
                        required=None,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('typeL',
                        type=str,
                        required=None,
                        help="This field cannot be left blank!"
                        )

    def get(self, designId):
        print("param ", designId)
        item = adapter.model.Models.LoadDao.find_by_designId(designId)
        if item:
            return item.json()
        return {'message': 'Item not found...'}, 404

    def post(self, designId):
        if adapter.model.Models.LoadDao.find_by_designId(designId):
            return {'message': "An item with designId '{}' already exists.".format(designId)}, 400
        print("antes de data ")
        data = self.parser.parse_args()
        print("la dataaaaaa", data)
        item = adapter.model.Models.LoadDao(**data)

        try:
            item.save_to_db()
            print("successfull saved it")
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201


class LoadList(Resource):

    def get(self):
        return {'items': list(map(lambda x: x.json(), adapter.model.Models.LoadDao.query.all()))}, 200

    def post(self):

        listLoads = list(request.get_json()['loadlist'])

        for item in listLoads:
            elem = adapter.model.Models.LoadDao(**item)
            try:
                elem.save_to_db()
                print("successfull saved it")

            except:
                return {"message": "An error occurred inserting the item."}, 500

        return {"message" : "succesfully saved them"}, 201
class ProjectResource(Resource):

    def get(self):
        return {'items': list(map(lambda x: x.json(), adapter.model.Models.Project.query.all()))}, 200

    def post(self):

        name = (request.get_json())


        elem = adapter.model.Models.Project(**name)
        try:
            elem.save_to_db()
            print("successfull saved it")

        except:
            return {"message": "An error occurred inserting the item."}, 500

        return {"message" : "succesfully saved them"}, 201


class Engine(Resource):

    def get(self, designId):

        print(designId)
        eng = Engineer()
        print('procesing batch name: ' + designId)
        eng.getListofLoad(designId)
        eng.calcDemandEnergy()
        eng.buildDataFrame()
        eng.calcSolarDesign()
        return {"message": "Sizing was ok"}, 201


