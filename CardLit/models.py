from CardLit import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100))
    answer = db.Column(db.String(100))
    correct = db.Column(db.Boolean)
    # box = db.relationship('Box', backref='Card', lazy='dynamic', foreign_keys='box.id')
    box_id = db.Column(db.Integer, db.ForeignKey('box.id'))


class Box(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proficiency_level = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100))
    # set = db.relationship('Set', backref='Box', lazy='dynamic', foreign_keys='Box.set_id')
    set_id = db.Column(db.Integer, db.ForeignKey('set.id'))


class Set(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
