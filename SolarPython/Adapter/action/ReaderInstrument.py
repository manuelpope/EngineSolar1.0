# Perform actions related to instruments
# as multimeter... Iload,Vload,AC or DC, PowerFactor and Hours per day
import json


class ReaderInstrument(object):
    def __init__(self, path=None):
        self.__pathJson = path
        self.dictLoad = {}

    def getMeasures(self):
        self.processJsonReader()
        return ( self.dictLoad.get("Load").get("voltage"),
                 self.dictLoad.get("Load").get("current"),
                 self.dictLoad.get("Load").get("workingHours"),
                 self.dictLoad.get("Load").get("powerFactor"),
                 self.dictLoad.get("Load").get("type"))

    def processJsonReader(self):
        with open(self.__pathJson, 'r') as f:
            self.dictLoad = json.load(f)
        return self.dictLoad
