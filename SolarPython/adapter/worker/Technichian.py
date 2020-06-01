# Use all data from Reader ,
# create electric schematics building loads and
# listing them. Storing all Loads in DB table.

import os

from adapter.action.BuilderLoad import BuilderLoad
from adapter.action.ReaderInstrument import ReaderInstrument


class Technichian(object):
    listDict = []

    def work(self):
        dir = os.path.dirname(__file__)
        dir = dir.replace("/adapter/worker", "")
        filename = os.path.join(dir, 'jsonTestData.json')
        readerx = ReaderInstrument(filename)
        builder = BuilderLoad(readerx)
        print(builder.buildLoad())
        print(builder.__str__())

    def reportToEngineDB(self, dictFromUILoad):
        self.listDict.append(dictFromUILoad)
        print(self.listDict)

    def saveAllListLoads(self):
        print("savind list")
        for elem in self.listDict:
            print(elem)
