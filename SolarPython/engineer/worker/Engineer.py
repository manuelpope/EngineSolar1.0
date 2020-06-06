import datetime

import numpy as np
import pandas as pd

import engineer.servicios
import engineer.servicios.ProviderEquipment
from engineer.Dao import DaoLoad


class Engineer(object):
    dataToProcess = []
    nameDesign = ""
    bigDict = {}

    def __init__(self):
        self.load = DaoLoad()

    def calculos(self):
        print(" calulando radios, diametros , oEM")

    def repotar(self):
        print("presentar reportes")

    def calcularcostos(self):
        print("esa m esta muy cara")

    def getListofLoad(self, nameDesign):

        date = str(datetime.datetime.now().strftime("%d-%b-%Y"))
        self.dataToProcess = (self.load.getBatchLoadsByBatchId(date + str(nameDesign)))
        print("mostrando la busqueda.....", len(self.dataToProcess))
        for elem in self.dataToProcess:
            print(elem)

        print('calculing energy')
        lisEnergy = self.calcDemandEnergy()
        totalEnergy = round(np.sum(lisEnergy), 3)
        print(totalEnergy)

    def energyCal(self, load):
        calc = load
        # print(load.__dict__)
        return round(calc.quantity * (
                (float(calc.workingHoursNight) + float(calc.workingHoursDay)) * float(calc.current) * float(
            calc.vx) / float(calc.pf)), 3)

    def calcDemandEnergy(self):
        energyPerDevice = [self.energyCal(elem) for elem in self.dataToProcess]
        # print('printing list of energy',energyPerDevice)
        return energyPerDevice

    def buildDataFrame(self):
        listBig = []
        for i in self.dataToProcess:
            listBig.append(i.listValues())
            print(str(i))
        arrayTodf = np.array(listBig)
        arrayTodf.reshape(len(self.dataToProcess), 8, -1)
        self.frame = pd.DataFrame(arrayTodf,
                                  columns=['id', 'voltage', 'current', 'pf', 'type', 'quantity', 'Hday', 'Hnight'])
        self.frame['voltage'] = self.frame['voltage'].astype('float64')
        self.frame['current'] = self.frame['current'].astype('float64')
        self.frame['pf'] = self.frame['pf'].astype('float64')
        self.frame['Hnight'] = self.frame['Hnight'].astype('float64')
        self.frame['Hday'] = self.frame['Hday'].astype('float64')
        self.frame['quantity'] = self.frame['quantity'].astype('int32')
        print(self.frame.dtypes)
        self.frame['EnergyWhDay'] = (self.frame['voltage'] * self.frame['current'] * self.frame['quantity'] *
                                     self.frame['Hday']) / self.frame['pf']
        self.frame['EnergyWhNight'] = (self.frame['voltage'] * self.frame['current'] * self.frame['quantity'] *
                                       self.frame['Hnight']) / self.frame['pf']
        print(self.frame.head())

    def calcSolarDesign(self):
        totalEnergyDia = np.sum(self.frame['EnergyWhDay'])
        totalEnergyNoche = np.sum(self.frame['EnergyWhNight'])

        print("Total energia Day : ")
        print(totalEnergyDia)
        print("Total energia Night : ")
        print(totalEnergyNoche)
        print("Total energia Day : ")
        print(totalEnergyDia + totalEnergyNoche)

        autonomia = np.round(totalEnergyNoche / totalEnergyDia)
        regulador = engineer.servicios.ProviderEquipment.getRegulator()
        inversor = engineer.servicios.ProviderEquipment.getInverter()
        panel = engineer.servicios.ProviderEquipment.getPanel()
        battery = engineer.servicios.ProviderEquipment.getBattery()
        powerOfArrPanels = np.round(totalEnergyDia / \
                                    (engineer.servicios.ProviderEquipment.getAreaFactor() * \
                                   (regulador.eff * inversor.eff)))
        quantityPanels = np.round(powerOfArrPanels / panel.power)
        minCurrentCapacity = np.round(totalEnergyNoche/panel.voltage/regulador.eff/inversor.eff)
        numBaterriesSeries = np.round(panel.voltage/battery.voltage)
        corrientMonoblockParalell = np.round((minCurrentCapacity/battery.dod))
        rowBatteries = np.round(corrientMonoblockParalell/battery.corriente)
        bateriasTotal = numBaterriesSeries * rowBatteries
        regulador.corrienteIn = round(panel.power* quantityPanels/panel.voltage)
        potenciaInversorMin = self.potenciaAC()
        regulador.corrienteOut =  potenciaInversorMin/inversor.eff/regulador.voltage
        minPotenciaSeleccionInversor = np.round(potenciaInversorMin*1.5)
        inversor.volIn= regulador.voltage
        print('full design')
        print(minPotenciaSeleccionInversor, bateriasTotal,quantityPanels,regulador.corrienteIn,autonomia)






    def potenciaAC (self):
        aux = self.frame.query('type == "AC"')
        return np.round(np.sum(aux['voltage']* aux['current']/aux['pf']))
