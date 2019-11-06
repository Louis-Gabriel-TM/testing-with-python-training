from db import db


class StoreModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        # Can be tested with an unit test
        self.name = name

    def json(self):
        # Interact with db -> integration test
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        # Interact with db -> integration test
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        # Interact with db -> integration test
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        # Interact with db -> integration test
        db.session.delete(self)
        db.session.commit()
