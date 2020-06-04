import app
from adapter.model.modelFlask import Load


class DaoLoad(object):
    pass

    @staticmethod
    def getAllLoads():

        return Load.query.all()

    @staticmethod
    def getLoadById(id):
        return Load.query.get(id)

    @staticmethod
    def getBatchLoadsByBatchId( bathId):
        return Load.query.filter_by(batchId=(str(bathId))).all()