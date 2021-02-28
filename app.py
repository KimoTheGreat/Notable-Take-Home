from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///physicians.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)


class physicians(db.Model):
    id = db.Column('physician_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    appointments = db.relationship('appointments', backref='physicians', lazy=True)

    def __init__(self, name):
        self.name = name

class appointments(db.Model):
    id = db.Column('appointment_id', db.Integer, primary_key = True)
    physician_id = db.Column(db.Integer, db.ForeignKey('physicians.physician_id'), nullable=False)
    patient_name = db.Column(db.String(100))
    appointment_time = db.Column(db.String(10))
    appointment_type = db.Column(db.String(20))

    def __init__(self, physician_id, patient_name, appointment_time, appointment_type):
        self.physician_id = physician_id
        self.patient_name = patient_name
        self.appointment_time = appointment_time 
        self.appointment_type = appointment_type


@app.route('/')
def get_all_physicians(select_physician=1):
    selected_physician_appointments = appointments.query.filter_by(physician_id=select_physician).all()
    return render_template('get_all_physicians.html', physicians = physicians.query.all(), appointments=selected_physician_appointments)

@app.route('/physician_appointments/<phys_id>')
def get_physician_appointments(phys_id):
    selected_physician_appointments = appointments.query.filter_by(physician_id=phys_id).all()
    return render_template('get_all_physicians.html', physicians = physicians.query.all(), appointments=selected_physician_appointments)

@app.route('/new_physician', methods = ['GET', 'POST'])
def new_physician():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Please enter the name of physician', 'error')
        else:
            physician = physicians(request.form['name'])

            db.session.add(physician)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('get_all_physicians'))
    return render_template('new_physician.html')

@app.route('/new_appointment', methods = ['GET', 'POST'])
def new_appointment():
    if request.method == 'POST':
        if not request.form['physician_id']:
            flash('Please enter all the appointment details!', 'error')
        else:
            physician_id = request.form['physician_id']
            patient_name = request.form['patient_name']
            appointment_time = request.form['appointment_time']
            appointment_type = request.form['appointment_type']
            appointment = appointments(physician_id, patient_name, appointment_time, appointment_type)

            db.session.add(appointment)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('get_all_physicians'))

    return render_template('new_appointment.html')

def add_dummy_data():
    """Function that runs once at the beginning to initialize dummy data"""
    # create fake physicians
    physician_1 = physicians("John Smith")
    physician_2 = physicians("Jane Doe")
    db.session.add(physician_1)
    db.session.add(physician_2)

    # create fake appointments
    dummy_appointment_1 = appointments(1, 'Kareem Tinawi', '8:00 am', "Check up")
    db.session.add(dummy_appointment_1)
    dummy_appointment_2 = appointments(1, 'Karim Tinawi', '10:00 am', "Check up")
    db.session.add(dummy_appointment_2)
    dummy_appointment_3 = appointments(1, 'Kareem Tinawi', '5:00 pm', "Follow up")
    db.session.add(dummy_appointment_3)


if __name__ == '__main__':
    db.create_all()
    db.session.commit()

    app.run(debug = True)
