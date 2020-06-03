from engineer.model.Battery import Battery
from engineer.model.Inverter import Inverter
from engineer.model.PhotoPanel import PhotoPanel
from engineer.model.Regulator import Regulator

panel = PhotoPanel()
panel.voltage = 24
panel.power = 230

regulador = Regulator()
regulador.voltaje = 24
regulador.eff = 0.85

inverter = Inverter()
inverter.eff = 0.95

battery = Battery()
battery.voltaje = 24
battery.dod = 0.30


def getBattery():
    return battery;

def getRegulator():
    return regulador

def getInverter():
    return inverter

def getPanel():
    return panel