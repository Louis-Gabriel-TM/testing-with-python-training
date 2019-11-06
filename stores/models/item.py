from db import db


class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        # Can be tested in an unit test
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        # Can be tested in an unit test
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # Interact with db -> integration test
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        # Interact with sb -> integration test
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        # Interact with db -> integration test
        db.session.delete(self)
        db.session.commit()
