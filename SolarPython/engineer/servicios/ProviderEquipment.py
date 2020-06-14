from engineer.model.Battery import Battery
from engineer.model.Inverter import Inverter
from engineer.model.PhotoPanel import PhotoPanel
from engineer.model.Regulator import Regulator



def getBattery():
    battery = Battery()
    battery.voltage = 12
    battery.corriente = 100
    battery.dod = 0.30
    return battery

def getRegulator():
    regulador = Regulator()
    regulador.voltage = 24
    regulador.eff = 0.85

    return regulador

def getInverter():
    inverter = Inverter()
    inverter.eff = 0.95
    return inverter

def getPanel():
    panel = PhotoPanel()
    panel.voltage = 24
    panel.power = 230
    return panel

def getAreaFactor():
    #fun to pass factor de area x  ip
    #now hard coded for Bogota
    return float(3.8)