# from flask import Flask, render_template, request, redirect, url_for, flash
# from data import add_patient, add_doctor, add_record, get_records, patients, doctors

# app = Flask(__name__)
# app.secret_key = "some_super_secret_key"

# @app.route('/')
# def home():
#     return render_template("home.html")
# # Patient registration route
# @app.route('/register/patient', methods=['GET', 'POST'])
# def register_patient():
#     if request.method == "POST":
#         name = request.form["name"].strip()
#         if name:
#             pid = add_patient(name)
#             flash(f"Patient registered successfully! ID: {pid}")
#             return redirect(url_for('view_patients'))
#         else:
#             flash("Please fill the patient name.")
#     return render_template("register_patient.html")

# # Doctor registration route
# @app.route('/register/doctor', methods=['GET', 'POST'])
# def register_doctor():
#     if request.method == "POST":
#         name = request.form["name"].strip()
#         if name:
#             did = add_doctor(name)
#             flash(f"Doctor registered successfully! ID: {did}")
#             return redirect(url_for('view_doctors'))
#         else:
#             flash("Please fill the doctor name.")
#     return render_template("register_doctor.html")


# @app.route('/add_record', methods=['GET', 'POST'])
# def add_record_form():
#     all_patients = list(patients.values())
#     all_doctors = list(doctors.values())
#     if request.method == "POST":
#         pid = request.form.get("patient_id", "").strip()
#         did = request.form.get("doctor_id", "").strip()
#         desc = request.form.get("description", "").strip()
#         data = request.form.get("data", "").strip()
#         if pid in patients and did in doctors and desc and data:
#             add_record(pid, did, desc, data)
#             flash("Health record added successfully!")
#             return redirect(url_for('search_patient_records'))
#         else:
#             flash("All fields are required.")
#     return render_template("add_record.html", all_patients=all_patients, all_doctors=all_doctors)

# @app.route('/patients')
# def view_patients():
#     return render_template("patients.html", patients=patients.values())

# @app.route('/doctors')
# def view_doctors():
#     return render_template("doctors.html", doctors=doctors.values())

# @app.route('/search_patient_records', methods=['GET', 'POST'])
# def search_patient_records():
#     records_for_patient = None
#     search_id = ""
#     if request.method == "POST":
#         search_id = request.form.get("patient_id", "").strip()
#         records_for_patient = get_records(search_id) if search_id else None
#     return render_template(
#         "search_patient_records.html",
#         records=records_for_patient,
#         search_id=search_id,
#         doctors=doctors
#     )

# if __name__ == "__main__":
#     app.run(debug=True)


#=========================================================================


import datetime

from models import HealthRecord 




from flask import Flask, render_template, request, redirect, url_for, flash
# from data import add_patient, add_doctor, add_record, get_records, patients, doctors

import datetime
from models import Patient, Doctor

def generate_patient_id():
    year = datetime.datetime.now().year
    last_patient = Patient.query.filter(Patient.id.like(f"{year}%")) \
                               .order_by(Patient.id.desc()).first()
    if last_patient:
        serial = int(last_patient.id[-4:]) + 1
    else:
        serial = 1
    return f"{year}{serial:04d}"

def generate_doctor_id():
    year = datetime.datetime.now().year
    last_doc = Doctor.query.filter(Doctor.id.like(f"%{year}")) \
                           .order_by(Doctor.id.desc()).first()
    if last_doc:
        serial = int(last_doc.id[:3]) + 1
    else:
        serial = 1
    return f"{serial:03d}{year}"




app = Flask(__name__)
app.secret_key = "your_secret_key_here"

from models import db, Patient, Doctor, HealthRecord

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ehr.db'
db.init_app(app)

# Create the DB/tables once, at startup:
with app.app_context():
    db.create_all()


@app.context_processor
def inject_now():
    return {'year': datetime.datetime.now().year}

@app.route('/')
def home():
    return render_template("home.html")



@app.route('/register/patient', methods=['GET', 'POST'])
def register_patient():
    if request.method == "POST":
        name = request.form["name"].strip()
        if name:
            pid = generate_patient_id()
            patient = Patient(id=pid, name=name)
            db.session.add(patient)
            db.session.commit()
            flash(f"Patient registered successfully! ID: {pid}")
            return redirect(url_for('view_patients'))
        else:
            flash("Please fill the patient name.")
    return render_template("register_patient.html")


@app.route('/register/doctor', methods=['GET', 'POST'])
def register_doctor():
    if request.method == "POST":
        name = request.form["name"].strip()
        if name:
            did = generate_doctor_id()
            doctor = Doctor(id=did, name=name)
            db.session.add(doctor)
            db.session.commit()
            flash(f"Doctor registered successfully! ID: {did}")
            return redirect(url_for('view_doctors'))
        else:
            flash("Please fill the doctor name.")
    return render_template("register_doctor.html")

# @app.route('/add_record', methods=['GET', 'POST'])
# def add_record_form():
#     all_patients = list(patients.values())
#     all_doctors = list(doctors.values())
#     if request.method == "POST":
#         pid = request.form.get("patient_id", "").strip()
#         did = request.form.get("doctor_id", "").strip()
#         desc = request.form.get("description", "").strip()
#         # data_ = request.form.get("data", "").strip() removed as per the latest context


#         allergy = request.form.get("allergy", "").strip()
#         medical_history = request.form.get("medical_history", "").strip()
#         family_history = request.form.get("family_history", "").strip()
#         vaccination = request.form.get("vaccination", "").strip()
#         vitals = request.form.get("vitals", "").strip()
#         lifestyle = request.form.get("lifestyle", "").strip()
#         medications = request.form.get("medications", "").strip()
#         emergency_contact = request.form.get("emergency_contact", "").strip()




@app.route('/add_record', methods=['GET', 'POST'])
def add_record_form():
    # fetch all patients/doctors from DB for population
    all_patients = Patient.query.all()
    all_doctors = Doctor.query.all()
    if request.method == "POST":
        record = HealthRecord(
            patient_id=request.form["patient_id"],
            doctor_id=request.form["doctor_id"],
            description=request.form["description"],
            data=request.form.get("data", ""),
            prescription=request.form.get("prescription", ""),
            symptoms=request.form.get("symptoms", ""),
            diagnosis=request.form.get("diagnosis", ""),
            lab_results=request.form.get("lab_results", ""),
            notes=request.form.get("notes", ""),
            followup=request.form.get("followup", "")
        )
        db.session.add(record)
        db.session.commit()
        flash("Health record added successfully!")
        return redirect(url_for('search_patient_records'))
    return render_template("add_record.html", all_patients=all_patients, all_doctors=all_doctors)

        
        




    if pid in patients and did in doctors and desc and allergy and medical_history and family_history and vaccination and vitals and lifestyle and medications and emergency_contact:
            add_record(pid, did, desc, allergy, medical_history, family_history, vaccination, vitals, lifestyle, medications, emergency_contact)
            flash("Health record added successfully!")
            return redirect(url_for('search_patient_records'))
    else:
            flash("All fields are required and must exist.")
    return render_template("add_record.html", all_patients=all_patients, all_doctors=all_doctors)

# @app.route('/patients')     old one
# def view_patients():
#     return render_template("patients.html", patients=patients.values())
@app.route('/patients')
def view_patients():
 
    # NEW (database):
    return render_template("patients.html", patients=Patient.query.all())


# @app.route('/doctors')     old one
# def view_doctors():
#     return render_template("doctors.html", doctors=doctors.values())


@app.route('/doctors')
def view_doctors():
  
    # NEW:
    return render_template("doctors.html", doctors=Doctor.query.all())

@app.route('/search_patient_records', methods=['GET', 'POST'])
def search_patient_records():
    records_for_patient = None
    search_id = ""
    doctor_dict = {d.id: d for d in Doctor.query.all()}
    if request.method == "POST":
        search_id = request.form.get("patient_id", "").strip()
        if search_id:
            records_for_patient = HealthRecord.query.filter_by(patient_id=search_id).all()
    return render_template(
        "search_patient_records.html",
        records=records_for_patient,
        search_id=search_id,
        doctors=doctor_dict
    )



if __name__ == "__main__":
    app.run(debug=True)
