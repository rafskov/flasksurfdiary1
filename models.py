from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    session_description = db.Column(db.String(100))
    waveheight = db.Column(db.Integer())
    waveperiod = db.Column(db.Integer())
    img = db.Column(db.Integer())






