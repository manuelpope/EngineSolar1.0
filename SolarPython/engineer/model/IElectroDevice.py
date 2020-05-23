from abc import ABC


class IElectroDevice(ABC):
    def input(self):
        pass

    def output(self):
        pass
