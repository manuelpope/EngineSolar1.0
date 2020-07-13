from db import db


class LoadDao(db.Model):
    __tablename__ = 'loadsapi'

    id = db.Column(db.Integer, primary_key=True)
    designId = db.Column(db.String(80))
    voltage = db.Column(db.Float(precision=2))
    current = db.Column(db.Float(precision=2))
    quantity = db.Column(db.Integer)


    def __init__(self, designId, voltage, current,quantity):
        self.designId = designId
        self.voltage = voltage
        self.current = current
        self.quantity = quantity

    def json(self):
        return {'design': self.designId, 'quantity': self.quantity}

    @classmethod
    def find_by_designId(cls, param):
        print("param " + param)
        result = cls.query.filter_by(designId = param).first()
        return result
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()