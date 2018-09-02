from app import db


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(120), nullable=True)
    deadline = db.Column(db.String(120), nullable=True)
    
