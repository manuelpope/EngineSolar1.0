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


    def __init__(self,nameDesign=None ,vx=0, current=0, hoursNight=0,hoursDay=0, px=1.0, typeL='AC',quantity=1):
        self.vx = vx
        self.current = current
        self.workingHoursDay = hoursDay
        self.workingHoursNight = hoursNight
        self.typeL = typeL
        self.px = px
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

    @property
    def px(self):
        return self.pf

    @px.setter
    def px(self, px):
        if self.typeL == 'DC':
            self.pf = 0.9
        else:
            self.pf = px

    def __str__(self):
        return str([self.id,self.vx, self.current, self.pf, self.typeL,
                    self.quantity,self.workingHoursDay,self.workingHoursNight])

    def listValues(self):
        return [self.id, self.vx, self.current, self.pf, self.typeL,
                    self.quantity, self.workingHoursDay, self.workingHoursNight]

    def saveLoad(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def getAllLoads(cls):

        return cls.query.all()
    @classmethod
    def getLoadById(cls,id):
        return cls.query.get(id)

    @classmethod
    def getBatchLoadsByBatchId(cls,bathId):
        return cls.query.filter_by(batchId=(str(bathId))).all()

