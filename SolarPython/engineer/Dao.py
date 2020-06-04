from adapter.model.modelFlask import Load
import app


class DaoLoad(object):
    pass

    def getAllLoads(self):

        return Load.query.all()

    def getLoadById(self,id):
        return Load.query.get(id)

    def getBatchLoadsByBatchId(self, bathId):
        return Load.query.filter_by(batchId=(str(bathId))).all()