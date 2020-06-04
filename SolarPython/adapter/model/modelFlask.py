from datetime import datetime

from app import db


# Creating model table for our CRUD database
class Load(db.Model, object):
    __tablename__ = "LOAD"
    id = db.Column(db.Integer, primary_key=True)
    __voltage = db.Column('voltage', db.String(100))
    current = db.Column(db.String(100))
    pf = db.Column(db.String(100))
    batchId=db.Column(db.String(100))
    workingHoursDay = db.Column(db.String(100))
    workingHoursNight = db.Column(db.String(100))
    typeL = db.Column(db.String(100))
    quantity = db.Column(db.Integer)


    def __init__(self,nameDesign=None ,vx=0, current=0, hoursNight=0,hoursDay=0, pf=1.0, typeL='AC',quantity=1):
        self.vx = vx
        self.current = current
        self.workingHoursDay = hoursDay
        self.workingHoursNight = hoursNight
        self.pf = pf
        self.typeL = typeL
        self.batchId = str(datetime.now().strftime("%d-%b-%Y"))+str(nameDesign)
        self.quantity=quantity


    @property
    def vx(self):
        return self.__voltage

    @vx.setter
    def vx(self, vx):
        if float(vx) > 500:
            self.__voltage = 100
        else:
            self.__voltage = float(vx)

    def __str__(self):
        return str([self.vx, self.current, self.pf, self.typeL])
