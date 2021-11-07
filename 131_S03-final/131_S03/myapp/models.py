from myapp import db


class City(db.Model):
    name = db.Column(db.String(64), index=True, primary_key=True)
    rank = db.Column(db.Integer)
    visited = db.Column(db.Boolean, default=False)

    def setRank(self, rank):
        self.rank = rank
