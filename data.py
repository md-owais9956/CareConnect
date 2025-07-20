# # # data.py
# # import datetime

# # patient_serial = {}  # Keeps track of last serial per year

# # doctor_serial = {}
# # patients = {}
# # doctors = {}
# # records = []
# # def add_patient(name):
# #     year = datetime.datetime.now().year
# #     serial = patient_serial.get(year, 0) + 1
# #     patient_serial[year] = serial
# #     patient_id = f"{year}{serial:04d}"
# #     patients[patient_id] = {"id": patient_id, "name": name}
# #     return patient_id

# # def add_doctor(name):
# #     year = datetime.datetime.now().year
# #     serial = doctor_serial.get(year, 0) + 1
# #     doctor_serial[year] = serial
# #     doctor_id = f"{year}{serial:04d}"
# #     doctors[doctor_id] = {"id": doctor_id, "name": name}
# #     return doctor_id


# # def add_record(patient_id, doctor_id, description, data):
# #     record = {
# #         "patient_id": patient_id,
# #         "doctor_id": doctor_id,
# #         "description": description,
# #         "data": data
# #     }
# #     records.append(record)

# # def get_records(patient_id):
# #     return [r for r in records if r["patient_id"] == patient_id]






# # -----------------------------------------------------------------------------------------------------------


# import datetime

# patients = {}
# doctors = {}
# records = []
# # Serial number tracking dictionaries
# patient_serial = {}
# doctor_serial = {}






# def add_patient(name):
#     year = datetime.datetime.now().year
#     serial = patient_serial.get(year, 0) + 1
#     patient_serial[year] = serial
#     patient_id = f"{year}{serial:04d}"
#     patients[patient_id] = {"id": patient_id, "name": name}
#     return patient_id


# def add_doctor(name):
#     year = datetime.datetime.now().year
#     serial = doctor_serial.get(year, 0) + 1
#     doctor_serial[year] = serial
#     doctor_id = f"{serial:03d}{year}"
#     doctors[doctor_id] = {"id": doctor_id, "name": name}
#     return doctor_id

# def add_record(patient_id, doctor_id, description, allergy, medical_history, family_history, vaccination, vitals, lifestyle, medications, emergency_contact ):
#     record = {
#         "patient_id": patient_id,
#         "doctor_id": doctor_id,
#         "description": description,
#         # "data": data,
#         "allergy": allergy,
#         "medical_history": medical_history,
#         "family_history": family_history,
#         "vaccination": vaccination,
#         "vitals": vitals,
#         "lifestyle": lifestyle,
#         "medications": medications,
#         "emergency_contact": emergency_contact
#     }
#     records.append(record)

# def get_records(patient_id):
#     return [r for r in records if r["patient_id"] == patient_id]



# # ========================================================================================


# # models.py

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Patient(db.Model):
#     id = db.Column(db.String(20), primary_key=True)
#     name = db.Column(db.String(120), nullable=False)

# class Doctor(db.Model):
#     id = db.Column(db.String(20), primary_key=True)
#     name = db.Column(db.String(120), nullable=False)

# class HealthRecord(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     patient_id = db.Column(db.String(20), db.ForeignKey('patient.id'))
#     doctor_id = db.Column(db.String(20), db.ForeignKey('doctor.id'))
#     description = db.Column(db.String(200))
#     data = db.Column(db.Text)
#     prescription = db.Column(db.Text)
#     symptoms = db.Column(db.Text)
#     diagnosis = db.Column(db.Text)
#     lab_results = db.Column(db.Text)
#     notes = db.Column(db.Text)
#     followup = db.Column(db.String(20))
#     # you can add more fields as needed
