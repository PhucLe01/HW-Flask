from myapp import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    rank = db.Column(db.Integer)
    visited = db.Column(db.Boolean, default=False)

