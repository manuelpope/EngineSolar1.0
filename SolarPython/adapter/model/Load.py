class Load(object):

    def __init__(self, voltage, current, pf=1.0, typeL = "AC"):
        self.__currentOperation = current
        self.__voltageOperation = voltage
        self.__pf = pf
        self.__type = typeL

    def __call__(self, *args, **kwargs):
        return self

    def __str__(self):
        return "voltage: {0}  ,current: {1}, power factor: {2}, type: {3}".format(self.__voltageOperation, self.__currentOperation, self.__pf,self.__type)
