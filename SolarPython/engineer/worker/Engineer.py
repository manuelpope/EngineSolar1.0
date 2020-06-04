import datetime
from engineer.Dao import DaoLoad
import numpy as np





class Engineer(object):
    dataToProcess=[]
    nameDesign=""
    def __init__(self):
        self.load =  DaoLoad()

    def calculos(self):
        print(" calulando radios, diametros , oEM")

    def repotar(self):
        print("presentar reportes")

    def calcularcostos(self):
        print("esa m esta muy cara")


    def getListofLoad(self,nameDesign):

        date = str(datetime.datetime.now().strftime("%d-%b-%Y"))
        self.dataToProcess=(self.load.getBatchLoadsByBatchId(date + str(nameDesign)))
        print("mostrando la busqueda.....", len(self.dataToProcess))
        for elem in self.dataToProcess:
            print(elem)

        print('calculing energy')
        lisEnergy = self.calcDemandEnergy()
        totalEnergy = round(np.sum(lisEnergy),3)
        print(totalEnergy)

    def energyCal(self,load):
        calc = load
        return round(((float(calc.workingHoursNight)+float(calc.workingHoursDay))*float(calc.current)*float(calc.vx)/float(calc.pf)),3)


    def calcDemandEnergy(self):
        energyPerDevice= [self.energyCal(elem) for elem in self.dataToProcess]
        #print('printing list of energy',energyPerDevice)
        return energyPerDevice
