import datetime

from engineer.Dao import DaoLoad

from adapter.model.modelFlask import Load
import app


class Engineer(object):
    pass

    def calculos(self):
        print(" calulando radios, diametros , oEM")

    def repotar(self):
        print("presentar reportes")

    def calcularcostos(self):
        print("esa m esta muy cara")


    def getListofLoad(self):

        dao = DaoLoad()
        dataToProcess=[]
        date = str(datetime.datetime.now().strftime("%d-%b-%Y"))
        dataToProcess.append(dao.getBatchLoadsById(date+'xx'))
        print("mostrando la busqueda.....")
        for i in dataToProcess:
            print(str(i))


