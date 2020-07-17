import datetime
from datetime import datetime

from db import db


class LoadDao(db.Model):
    __tablename__ = 'loadsapi'

    id = db.Column(db.Integer, primary_key=True)
    designId = db.Column(db.String(80))
    voltage = db.Column(db.Float(precision=2))
    current = db.Column(db.Float(precision=2))
    quantity = db.Column(db.Integer)
    pf = db.Column(db.Float(precision=2))
    workingHoursDay = db.Column(db.Float(precision=2))
    workingHoursNight = db.Column(db.Float(precision=2))
    typeL = db.Column(db.String(100))

    def __init__(self, designId, voltage, current, quantity, pf, workingHoursDay, workingHoursNight, typeL):
        self.designId = designId
        self.voltage = voltage
        self.current = current
        self.quantity = quantity
        self.pf = pf
        self.workingHoursDay = workingHoursDay
        self.workingHoursNight = workingHoursNight
        self.typeL = typeL

    def json(self):
        return {'design': self.designId, 'voltage': self.voltage,
                'current': self.current,
                'quantity': self.quantity,
                'pf': self.pf,
                'workingHoursDay': self.workingHoursDay,
                'workingHoursNight': self.workingHoursNight,
                'typeL': self.typeL
                }

    @classmethod
    def find_by_designId(cls, param):
        print("param " + param)
        result = cls.query.filter_by(designId=param).all()
        return result

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    designId = db.Column(db.String(80))
    voltage = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __init__(self, designId, voltage):
        self.designId = designId
        self.voltage = self.range(voltage)
        self.date = datetime.now().date()

    def json(self):
        return {'designId': self.designId,
                'date': str(self.date),
                'voltage': self.voltage
                }
    def range(self,voltage):
        p = lambda voltage: 110 if voltage <= 120 else (220 if voltage < 380 else 380)
        return p(voltage)
    @classmethod
    def find_by_designId(cls, param):
        print("param :" + param)
        result = cls.query.filter_by(designId=param).first_or_404()
        return result

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
