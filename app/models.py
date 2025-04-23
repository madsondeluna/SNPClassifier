from app import db
from datetime import datetime

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    vcf_filename = db.Column(db.String(200))
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    variants = db.relationship('Variant', backref='patient', lazy=True)

class Variant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    chromosome = db.Column(db.String(10))
    position = db.Column(db.Integer)
    ref = db.Column(db.String(10))
    alt = db.Column(db.String(10))
    gene = db.Column(db.String(50))
    consequence = db.Column(db.String(100))
    impact = db.Column(db.String(50))
    sift = db.Column(db.String(50))
    polyphen = db.Column(db.String(50))
    af = db.Column(db.Float)
    classification = db.Column(db.String(50))