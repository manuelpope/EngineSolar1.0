# Use all data from Reader ,
# create electric schematics building loads and
# listing them. Storing all Loads in DB table.

from adapter.action.ReaderInstrument import ReaderInstrument
from adapter.action.BuilderLoad import BuilderLoad
import os
class Technichian(object):
    pass

    def work(self):
        dir = os.path.dirname(__file__)
        dir = dir.replace("/adapter/worker", "")
        filename = os.path.join(dir, 'jsonTestData.json')
        readerx = ReaderInstrument(filename)
        builder = BuilderLoad(readerx)
        print(builder.buildLoad())
        print(builder.__str__())


if __name__ == '__main__':
    tech = Technichian()
    tech.work()