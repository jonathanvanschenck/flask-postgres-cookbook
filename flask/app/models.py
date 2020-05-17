from app import db

class Views(db.Model):
    id = db.Column(db.Integer, primary_key=True)
