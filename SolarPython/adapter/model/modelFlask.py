from app import db


# Creating model table for our CRUD database
class Load(db.Model, object):
    __tablename__ = "LOAD"
    id = db.Column(db.Integer, primary_key=True)
    __voltage = db.Column('voltage', db.String(100))
    current = db.Column(db.String(100))
    pf = db.Column(db.String(100))
    workingHours = db.Column(db.String(100))
    typeL = db.Column(db.String(100))

    def __init__(self, vx=0, current=0, hours=0):
        self.vx = vx
        self.current = current
        self.workingHours = hours

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
        return str([self.vx, self.current, self.pf, self.typeL,self.workingHours])
