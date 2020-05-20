# Build  Load from electric measurements , mapping service, takes a load and
# build it from signals of all ReaderInstruments
# TODO
# this class should be Static , it's collaborator, it can not be initialized !

from Adapter.model.Load import Load
from math import ceil


class BuilderLoad(object):

    def __init__(self, reader=None):
        self.__readerInstrument = reader
        self.__energyWh = 0
        self.__hours = 0
        self.__load = None

    def buildLoad(self):
        # method to convert json to object Load
        voltaje, current, self.__hours, pf , type = self.__readerInstrument.getMeasures()
        self.__load = Load(voltaje, current, pf, type)
        self.__energyWh = ceil(voltaje * current * self.__hours / pf)


        return "finished calculation Building"

    def loadGetter(self):
        return self.__load

    def energyGetter(self):
        return self.__energyWh

    def __str__(self):
        return "Load : {0} , Required Energy : {1} Wh, time : {2} h".format(self.__load, self.__energyWh, self.__hours)
