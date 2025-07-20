# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(120), nullable=False)

class Doctor(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(120), nullable=False)

class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.String(20), db.ForeignKey('patient.id'))
    doctor_id = db.Column(db.String(20), db.ForeignKey('doctor.id'))
    description = db.Column(db.String(200))
    data = db.Column(db.Text)
    prescription = db.Column(db.Text)
    symptoms = db.Column(db.Text)
    diagnosis = db.Column(db.Text)
    lab_results = db.Column(db.Text)
    notes = db.Column(db.Text)
    followup = db.Column(db.String(20))
    # you can add more fields as needed
