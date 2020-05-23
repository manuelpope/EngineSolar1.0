# Use all data from Reader ,
# create electric schematics building loads and
# listing them. Storing all Loads in DB table.

from Adapter.action.ReaderInstrument import ReaderInstrument
from Adapter.action.BuilderLoad import BuilderLoad


if __name__ == '__main__':
    readerx = ReaderInstrument("/Users/manueltobon/SolarPython/jsonTestData.json")
    builder = BuilderLoad(readerx)
    print(builder.buildLoad())
    print(builder.__str__())