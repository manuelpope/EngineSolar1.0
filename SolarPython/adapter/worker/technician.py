# Use all data from Reader ,
# create electric schematics building loads and
# listing them. Storing all Loads in DB table.

import os

from flask import flash

from adapter.action.BuilderLoad import BuilderLoad
from adapter.action.ReaderInstrument import ReaderInstrument
from app import db


class Technician(object):
    listDict = []

    def work(self):
        dir = os.path.dirname(__file__)
        dir = dir.replace("/adapter/worker", "")
        filename = os.path.join(dir, 'jsonTestData.json')
        readerx = ReaderInstrument(filename)
        builder = BuilderLoad(readerx)
        print(builder.buildLoad())
        print(builder.__str__())

    def reportToEngineerDB(self, dictFromUILoad):
        readerx = ReaderInstrument(dictFromUILoad)
        builder = BuilderLoad(readerx)
        builder.buildLoad()
        self.listDict.append(builder.loadGetter())
        print(builder.__str__())

    def saveAllListLoads(self):
        print("savind list")
        for elem in self.listDict:
            print(str(elem))
            db.session.add(elem)
            db.session.commit()
        flash("Employee Inserted Successfully")
