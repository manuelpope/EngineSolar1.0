# Perform actions related to instruments
# as multimeter... Iload,Vload,AC or DC, PowerFactor and Hours per day
import json


class ReaderInstrument(object):
    def __init__(self, dictionaryFromUI, path=None):
        self.__pathJson = path
        self.dictLoad = dictionaryFromUI

    def getMeasures(self):
        return (self.dictLoad.get("voltage"),
                self.dictLoad.get("current"),
                self.dictLoad.get("hours"),
                self.dictLoad.get("pf"),
                self.dictLoad.get("typeLoad"))

    def processJsonReader(self):
        with open(self.__pathJson, 'r') as f:
            self.dictLoad = json.load(f)
        return self.dictLoad
